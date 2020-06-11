import numpy as np
from statistics import harmonic_mean
import math
import matplotlib.pyplot as plt

import matplotlib.gridspec as gridspec


#def bootstrap(data, n=1000, func=np.mean):
#    """
#    Generate `n` bootstrap samples, evaluating `func`
#    at each resampling. `bootstrap` returns a function,
#    which can be called to obtain confidence intervals
#    of interest.
#    """
#    simulations = list()
#    sample_size = len(data)
#    xbar_init = np.mean(data)
#    
#    for c in range(n):
#        itersample = np.random.choice(data, size=sample_size, replace=True)
#        simulations.append(func(itersample))
#    simulations.sort()
#    def ci(p):
#        """
#        Return 2-sided symmetric confidence interval specified
#        by p.
#        """
#        u_pval = (1+p)/2.
#        l_pval = (1-u_pval)
#        l_indx = int(np.floor(n*l_pval))
#        u_indx = int(np.floor(n*u_pval))
#        return(simulations[l_indx],simulations[u_indx])
#    return(ci)

def example_plot(ax,a1, a2,t):
    ax.plot(a1,'r:',a2,'b--')

    #ax.locator_params(nbins=3)
    ax.set_xlabel('K-value', fontsize=12)
    ax.set_ylabel('Data', fontsize=12)
    ax.set_title(t, fontsize=12)




def bsample(data, n):
    simulations = list()
    sample_size = len(data)
    
    for c in range(n):
        itersample = np.random.choice(data, size=sample_size, replace=True)
        simulations.append(itersample)
    return simulations


data = [161.36, 159.89, 159.22, 160.63, 160.18, 158.6, 158.98, 158.15, 162.0, 159.6, 160.4, 160.9, 160.98, 160.61, 158.71, 160.9, 161.0, 161.09, 158.98, 161.81, 161.45, 160.69, 162.24, 160.49, 160.7, 160.85, 159.9, 159.61, 159.95, 159.76]

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





