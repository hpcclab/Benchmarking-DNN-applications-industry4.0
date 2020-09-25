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


data = [1.592783505154639, 1.5825864276568502, 1.592783505154639, 1.5968992248062015, 1.578544061302682, 1.6072821846553964, 1.588688946015424, 1.6568364611260054, 1.6524064171122992, 1.6816326530612244, 1.648, 1.6793478260869563, 1.5846153846153845, 1.6284584980237153, 1.6284584980237153, 1.4963680387409202, 1.6010362694300517, 1.511002444987775, 1.641434262948207, 1.6135770234986944, 1.6114732724902217, 1.6135770234986944, 1.5968992248062015, 1.6156862745098037, 1.6263157894736842, 1.6135770234986944, 1.6657681940700808, 1.6524064171122992, 1.6458055925432755, 1.6816326530612244]

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





