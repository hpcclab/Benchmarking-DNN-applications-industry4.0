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

with open('ResultofUCIANN.txt') as f:
    lines = f.read().splitlines()
    
  
print(lines)


i=0
for x in lines:
    #x=x.split('s')[0]
    lines[i]=float('%1.2f'%(float(x)))
    i=i+1
    
mean = np.mean(lines, axis=0)
std = np.std(lines, axis=0)

f = open("MeanSTD.txt", "a")
print(lines)
print("mean:",mean, " std: ",std)
f.write("mean: {0}s and  std: {1}s\n".format(mean,std))

f.close()
