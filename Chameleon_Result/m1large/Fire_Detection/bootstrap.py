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


data = [116.81625115420128, 121.76323387872954, 118.1802895843064, 117.85002328830926, 118.40149742629853, 127.27565392354124, 118.12511671335199, 117.74034434620754, 122.94655004859086, 119.1261770244821, 118.23551401869159, 121.64615384615384, 117.41252900232017, 117.79515828677839, 123.06614785992218, 116.49355432780847, 117.74034434620754, 123.42634146341463, 123.54687499999999, 118.73486625997184, 117.85002328830926, 118.40149742629853, 119.23845428840715, 120.8328557784145, 121.52929875120076, 119.74633222905821, 114.85428960508396]

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





