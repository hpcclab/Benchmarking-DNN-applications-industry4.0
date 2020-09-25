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


data = [91.57546145494028, 155.70646153846155, 153.34727272727272, 153.62659380692168, 158.53571428571428, 158.04059962523422, 151.05850746268658, 161.88291746641073, 156.18703703703704, 158.139375, 152.69945684972842, 154.47069597069597, 159.23410950283196, 155.89833641404806, 156.67058823529413, 150.60892857142858, 154.18829981718466, 160.34410646387835, 155.89833641404806, 158.93404522613065]

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





