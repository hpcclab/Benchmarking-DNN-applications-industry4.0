import scipy
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt

class Distribution(object):
    
    def __init__(self,dist_names_list = []):
        self.dist_names = ['norm','lognorm','expon']
        self.dist_results = []
        self.params = {}
        
        self.DistributionName = ""
        self.PValue = 0
        self.Param = None
        
        self.isFitted = False
        
        
    def Fit(self, y):
        self.dist_results = []
        self.params = {}
        for dist_name in self.dist_names:
            dist = getattr(scipy.stats, dist_name)
            param = dist.fit(y)
            
            self.params[dist_name] = param
            #Applying the Kolmogorov-Smirnov test
            D, p = scipy.stats.kstest(y, dist_name, args=param);
            self.dist_results.append((dist_name,p))
        #select the best fitted distribution
        sel_dist,p = (max(self.dist_results,key=lambda item:item[1]))
        #store the name of the best fit and its p value
        self.DistributionName = sel_dist
        self.PValue = p
        
        self.isFitted = True
        return self.DistributionName,self.PValue
    
    def Random(self, n = 1):
        if self.isFitted:
            dist_name = self.DistributionName
            param = self.params[dist_name]
            #initiate the scipy distribution
            dist = getattr(scipy.stats, dist_name)
            return dist.rvs(*param[:-2], loc=param[-2], scale=param[-1], size=n)
        else:
            raise ValueError('Must first run the Fit method.')
            
    def Plot(self,y):
        x = self.Random(n=len(y))
        plt.hist(x, alpha=0.5, label='Fitted')
        plt.hist(y, alpha=0.5, label='Actual')
        plt.legend(loc='upper right')
        plt.savefig("distrib.pdf")


from scipy.stats import expon
#r = expon.rvs(size=5000) #exponential
data = [22.13, 22.42, 22.23, 21.89, 28.9, 28.99, 29.11, 23.28, 26.47, 25.27, 23.08, 27.52, 26.78, 25.63, 23.28, 26.54, 26.44, 22.89, 22.36, 22.24, 22.68, 22.38, 22.4, 22.36, 22.03, 22.7, 22.76, 22.5, 22.81, 22.75]
dst = Distribution()
f = open("Kolmogorov_Smirnov_test.txt", "a")
print(dst.Fit(data))
f.write(str(dst.Fit(data)))
dst.Plot(data)
f.close()
