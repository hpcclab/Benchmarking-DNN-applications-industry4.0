#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:02:52 2019

@author: c00303945
"""
#f = open('ResultUCIML.txt', 'r')
#x = f.readlines()
#print(x)

import numpy as np

alist = [] 

with open('AIresult.txt') as f:
    lines = f.read().splitlines()
    
  
print(lines)


i=0
for x in lines:
    #x=x.split('s')[0]
    lines[i]=float('%1.2f'%(float(x)))*183.572130
    i=i+1
    
mean = np.mean(lines, axis=0)
std = np.std(lines, axis=0)

f = open("MeanSTD.txt", "a")
print(lines)
print("mean:",mean, " std: ",std)
f.write("mean MI: {0} and  std MI: {1}\n".format(mean,std))

f.close()
