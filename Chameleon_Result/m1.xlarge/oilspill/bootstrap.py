import numpy as np
from statistics import harmonic_mean
import math
import matplotlib.pyplot as plt

import matplotlib.gridspec as gridspec

def bsample(data, n):
    simulations = list()
    sample_size = len(data)
    
    for c in range(n):
        itersample = np.random.choice(data, size=sample_size, replace=True)
        simulations.append(itersample)
    return simulations


data = [247.28729281767957, 246.6060606060606, 240.8556053811659, 243.03529411764703, 243.47597461468723, 243.03529411764703, 243.25543478260872, 247.74354243542436, 248.6611111111111, 247.0597976080957, 248.43108233117482, 246.37981651376145, 243.03529411764703, 243.47597461468723, 241.50539568345326, 245.70356816102472, 245.92857142857142, 246.6060606060606, 246.153987167736, 245.25479452054796, 245.25479452054796, 247.28729281767957, 242.5962059620596, 247.5152073732719, 247.74354243542436, 246.6060606060606, 247.28729281767957, 243.47597461468723, 243.47597461468723, 245.47897623400365]

i=100
bbb = bsample(data,i)    
harmList = list()
for x in bbb:
    harmList.append(harmonic_mean(x))

harmList.sort()
alpha = 0.05

lower = math.ceil((alpha/2)*i)
upper = math.floor((1-(alpha/2))*i)

c1=harmList[lower]
c2=harmList[upper]
    
print(" Lower : ",c1)

print(" Upper: ",c2)

f = open("CI_Bootstrap.txt", "a")
f.write("\n C1: {0:.4f}s and  C2: {1:.4f}s\n".format(c1,c2))





