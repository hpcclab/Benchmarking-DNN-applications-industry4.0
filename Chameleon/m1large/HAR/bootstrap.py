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


data = [1.1423290203327172, 1.2249752229930624, 1.1693472090823083, 1.220138203356367, 1.2625127681307458, 1.2035053554040895, 1.2716049382716048, 1.129798903107861, 1.2888425443169969, 1.2955974842767297, 1.2848232848232848, 1.1704545454545454, 1.1605633802816901, 1.2237623762376237, 1.197674418604651, 1.294240837696335, 1.2650972364380757, 1.2888425443169969, 1.3010526315789472, 1.2129538763493621, 1.3051742344244983, 1.1095152603231597, 1.1339449541284403, 1.243460764587525, 1.2035053554040895, 1.2310756972111554, 1.105545617173524, 1.0189612530915086, 1.2347652347652347, 1.1884615384615385]

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





