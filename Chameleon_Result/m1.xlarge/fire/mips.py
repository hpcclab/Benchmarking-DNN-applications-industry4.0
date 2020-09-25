"""
Created on Mon Nov  4 15:02:52 2019

@author: c00303945
"""
#f = open('ResultUCIML.txt', 'r')
#x = f.readlines()
#print(x)

import numpy as np

alist = [] 

with open('ResultoFireDetection.txt') as f:
    lines = f.read().splitlines()

i=0
for x in lines:
    #x=x.split('s')[0]
    lines[i]=float('%1.2f'%(2530.24/float(x)))
    i=i+1
    
print(lines)

mean = np.mean(lines, axis=0)
std = np.std(lines, axis=0)

f = open("MeanStdMips.txt", "a")
#f.write(lines)
print("mean:",mean, " std: ",std)
for m in lines:
	f.write(str(m))
	f.write(", ")

f.write("\n mean of mips : {0}s and  std: {1}s\n".format(mean,std))

f.close()
