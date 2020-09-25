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


data = [1.503649635036496, 1.5527638190954773, 1.415807560137457, 1.525925925925926, 1.545, 1.3918918918918917, 1.4174311926605503, 1.4891566265060239, 1.5685279187817258, 1.5073170731707317, 1.4141876430205949, 1.4627218934911244, 1.4490035169988278, 1.5488721804511276, 1.474940334128878, 1.4820143884892085, 1.362734288864388, 1.5054811205846526, 1.603112840466926, 1.4272517321016165, 1.516564417177914, 1.4190585533869113, 1.4456140350877191, 1.4439252336448596, 1.3051742344244983, 1.4541176470588235, 1.4305555555555554, 1.5147058823529411, 1.5278121137206426, 1.570520965692503]

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





