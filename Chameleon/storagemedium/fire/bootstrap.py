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


data = [123.06614785992218, 118.06999533364441, 117.3036624942049, 122.47047434656339, 123.6676441837732, 123.72811735941319, 122.11583011583011, 123.97060264576187, 119.74633222905821, 122.76758854924793, 128.0485829959514, 125.50793650793649, 118.06999533364441, 122.88683827100533, 122.64857004362578, 118.12511671335199, 107.89936034115138, 122.11583011583011, 123.84924131179636, 119.74633222905821, 122.76758854924793, 128.0485829959514, 117.57620817843865, 123.84924131179636, 119.74633222905821, 122.76758854924793, 128.0485829959514, 119.63309692671395, 128.7653944020356, 128.2432843385707]

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





