# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:12:10 2019

@author: c00221719
"""
import time
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import keras
from sklearn import metrics
from keras.models import Sequential #sequential is required to initialise the neural network
from keras.layers import Dense      #dense is used to build the layers
from keras.layers import Dropout    #Dropout Layer in order to prevent Regularization in the network

#start_time = time.time()

xtrain=pd.read_table(r'X_train.txt',delim_whitespace=True,header=None)
xtest=pd.read_table(r'X_test.txt',delim_whitespace=True,header=None)
ytrain=pd.read_table(r'y_train.txt',header=None)
ytest=pd.read_table(r'y_test.txt',header=None)

xtrain=xtrain.values #converting into array
xtest=xtest.values

onehotencoder = OneHotEncoder()
ytrain = onehotencoder.fit_transform(ytrain).toarray()

#Initialising the deep learning model
#Defining the model as a sequence of layers
classifier = Sequential()
classifier.add(Dense(48, input_dim = 561, kernel_initializer='uniform', activation='relu', ))
#creating a network of 561 X 48 X 24 X 12 X6
classifier.add(Dropout(0.1))
classifier.add(Dense(24, kernel_initializer='uniform', activation='relu'))
classifier.add(Dropout(0.1))
classifier.add(Dense(12, kernel_initializer='uniform', activation='relu'))
classifier.add(Dropout(0.1))
classifier.add(Dense(6, kernel_initializer='uniform', activation='softmax'))
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics = ['accuracy'])
#Fitting the ANN to the training set
classifier.fit(xtrain, ytrain, batch_size=20, epochs=10, verbose = 4)

classifier.summary()

start_time = time.time()
pred = classifier.predict(xtest)
predictions = []
for i in range(len(pred)):
    predictions.append(pred[i].argmax() + 1)
    
print ("accuracy score %s" % (metrics.accuracy_score(ytest, predictions)*100))
tt = time.time()
print("--- Execution time : %s seconds ---" % (tt-start_time))

f = open("ResultofUCIANN.txt", "a")
f.write("{0}\n".format(tt-start_time))
f.close()

