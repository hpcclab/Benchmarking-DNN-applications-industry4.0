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


data = [121.35291459557163, 119.78322925958965, 120.80701754385964, 122.68341708542714, 92.92525951557094, 92.63677130044843, 92.25489522500858, 115.3582474226804, 101.45598791084247, 106.27384250098932, 116.3578856152513, 97.58502906976744, 100.28155339805825, 104.78111587982833, 115.3582474226804, 101.18839487565938, 101.57110438729198, 117.32372214941022, 120.1046511627907, 120.75269784172663, 118.41005291005291, 119.99731903485255, 119.89017857142858, 120.1046511627907, 121.90376758965047, 118.3057268722467, 117.99384885764498, 119.35733333333333, 117.73520385795705, 118.04571428571428]

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





