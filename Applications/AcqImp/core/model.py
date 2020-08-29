# Script defines the TCN model to train the network on

import torch
import torch.nn as nn
from torch.nn.utils import weight_norm
import torch.nn.functional as F

class Chomp1d(nn.Module):
    def __init__(self, chomp_size):
        super(Chomp1d, self).__init__()
        self.chomp_size = chomp_size

    def forward(self, x):
        return x[:, :, :-self.chomp_size].contiguous()


class TemporalBlock(nn.Module):
    def __init__(self, n_inputs, n_outputs, kernel_size, stride, dilation, padding, dropout=0.2):
        super(TemporalBlock, self).__init__()
        self.conv1 = weight_norm(nn.Conv1d(n_inputs, n_outputs, kernel_size,
                                           stride=stride, padding=padding, dilation=dilation, bias=True))
        self.chomp1 = Chomp1d(padding)
        self.relu1 = nn.ReLU()
        self.dropout1 = nn.Dropout(dropout)

        self.conv2 = weight_norm(nn.Conv1d(n_outputs, n_outputs, kernel_size,
                                           stride=stride, padding=padding, dilation=dilation, bias=True))
        self.chomp2 = Chomp1d(padding)
        self.relu2 = nn.ReLU()
        self.dropout2 = nn.Dropout(dropout)

        self.net = nn.Sequential(self.conv1, self.chomp1, self.relu1, self.dropout1,
                                 self.conv2, self.chomp2, self.relu2, self.dropout2)
        self.downsample = nn.Conv1d(n_inputs, n_outputs, 1, bias=True) if n_inputs != n_outputs else None
        self.relu = nn.ReLU()
        self.init_weights()

    def init_weights(self):
        self.conv1.weight.data.normal_(0, 0.01)
        self.conv2.weight.data.normal_(0, 0.01)
        if self.downsample is not None:
            self.downsample.weight.data.normal_(0, 0.01)

    def forward(self, x):
        out = self.net(x)
        res = x if self.downsample is None else self.downsample(x)
        return self.relu(out + res)


class TemporalConvNet(nn.Module):
    def __init__(self, num_inputs, num_channels, kernel_size=2, dropout=0.2):
        super(TemporalConvNet, self).__init__()
        layers = []
        num_levels = len(num_channels)
        for i in range(num_levels):
            dilation_size = 2 ** i
            in_channels = num_inputs if i == 0 else num_channels[i-1]
            out_channels = num_channels[i]
            layers += [TemporalBlock(in_channels, out_channels, kernel_size, stride=1, dilation=dilation_size,
                                     padding=(kernel_size-1) * dilation_size, dropout=dropout)]

        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)


class TCN(nn.Module):
    def __init__(self, input_size, output_size, num_channels, kernel_size, dropout):
        super(TCN, self).__init__()
        self.tcn = TemporalConvNet(input_size, num_channels, kernel_size=kernel_size, dropout=dropout)
        self.global_residual = nn.Conv1d(input_size, output_size, kernel_size=1)  # Global skip from input to last layer
        self.deconv1 = nn.ConvTranspose1d(7, 5, kernel_size=5, stride=2, padding=2)
        self.deconv2 = nn.ConvTranspose1d(5, 1, kernel_size=6, stride=2, padding=1, dilation=1)
        self.out = nn.Linear(num_channels[-1]+1, output_size)
        self.weight_init_res()

    def weight_init_res(self):
        self.global_residual.weight.data.normal_(0, 0.01)

    def forward(self, inputs):
        """Inputs have to have dimension (N, C_in, L_in)"""
        y = self.tcn(inputs)  # input should have dimension (N, C, L)
        y = torch.cat((y, inputs), dim=1)
        y = F.relu(self.deconv1(y))
        y = self.deconv2(y)
        out = y
        #out = self.out(y.transpose(1, 2)).transpose(1, 2)
        return out


class ANN(nn.Module):
    def __init__(self):
        super(ANN, self).__init__()
        self.ann1 = nn.Linear(500, 600)
        self.ann2 = nn.Linear(600, 600)
        self.ann3 = nn.Linear(600, 500)

    def forward(self, inputs):  # inputs have to be (N, *, in_features)
        N,C,L = inputs.shape
        a1 = torch.sigmoid(self.ann1(inputs))
        a2 = torch.sigmoid(self.ann2(a1))
        a3 = self.ann3(a2)

        return a3


class lstm(nn.Module):
    def __init__(self):
        super(lstm, self).__init__()
        self.lstm1 = nn.LSTM(input_size=1, hidden_size=20, batch_first=True, bidirectional=True)
        self.ann = nn.Linear(40, 1)
        self.deconv1 = nn.ConvTranspose1d(1, 5, kernel_size=5, stride=2, padding=2)
        self.deconv2 = nn.ConvTranspose1d(5, 1, kernel_size=6, stride=2, padding=1, dilation=1)

    def forward(self, inputs):  # inputs have to be (N,L,C)
        inputs = inputs.transpose(1, 2)
        a1,_ = self.lstm1(inputs)
        a2 = self.ann(a1)
        a2 = F.relu(a2.transpose(2,1))
        a3 = F.relu(self.deconv1(a2))
        a4 = self.deconv2(a3)

        return a4

