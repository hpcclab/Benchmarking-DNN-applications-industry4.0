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


data = [85.36538461538461, 119.35047169811321, 117.79469273743017, 123.00583373845406, 121.99758919961428, 125.32095096582466, 125.44521566683191, 123.18549172346641, 125.8820895522388, 125.19693221177634, 123.36567528035104, 123.97011268985791, 123.54638671875, 126.00747011952193, 129.75538461538463, 121.58721768380587, 121.70418470418471, 137.58727569331157, 130.2228512609367, 122.41074020319303, 121.23766171538092, 123.97011268985791, 127.33920483140412, 122.76710334788937, 124.58050221565732, 123.2454943984413, 121.35395683453237, 125.50744047619048, 140.41231964483907, 130.82885211995864]

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





