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


data = [1.0747826086956522, 0.9809523809523809, 1.1115107913669064, 1.0573139435414884, 1.1423290203327172, 1.1455050973123262, 1.1256830601092895, 1.1145175834084762, 1.087071240105541, 1.0785340314136125, 1.0369127516778522, 1.1085201793721973, 1.1236363636363635, 1.1095152603231597, 1.0377833753148613, 1.0804195804195804, 1.1412742382271468, 0.9895916733386709, 1.1465677179962894, 1.1339449541284403, 1.0627687016337057, 1.115523465703971, 0.7928159076330981, 1.1476323119777159, 0.9493087557603687, 1.0947741364038972, 1.1583880037488286, 1.1884615384615385, 1.1573033707865168, 1.0794759825327511]

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





