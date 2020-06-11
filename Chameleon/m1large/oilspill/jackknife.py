import numpy as np
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats
from statistics import harmonic_mean
import math

#data = np.array([1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40])
data = np.array([121.35291459557163, 119.78322925958965, 120.80701754385964, 122.68341708542714, 92.92525951557094, 92.63677130044843, 92.25489522500858, 115.3582474226804, 101.45598791084247, 106.27384250098932, 116.3578856152513, 97.58502906976744, 100.28155339805825, 104.78111587982833, 115.3582474226804, 101.18839487565938, 101.57110438729198, 117.32372214941022, 120.1046511627907, 120.75269784172663, 118.41005291005291, 119.99731903485255, 119.89017857142858, 120.1046511627907, 121.90376758965047, 118.3057268722467, 117.99384885764498, 119.35733333333333, 117.73520385795705, 118.04571428571428])

#data = np.array([1,2,3,4,5,6,7,8,9,0])

harmonica = harmonic_mean(data)

resamples = jackknife_resampling(data)

#print(resamples)

print(resamples.shape)


hrList = []

for x in resamples:
    hrList.append(harmonic_mean(x))



#print(" Hermonic mean list : ",hrList)

print(" Arithmetic mean of harmonic means ",np.mean(hrList))

hmean = np.mean(hrList)

sd = 0
for x in hrList:
    sd = sd + (x-hmean) ** 2

n = len(data)

tsd = sd*(n-1)

std = math.sqrt(tsd)


print(" Standard deviation of harmonic means ",std)


t = 2.045

c1 = harmonica - ((t*std)/math.sqrt(n))

c2 = harmonica + ((t*std)/math.sqrt(n))

print(" Confidence interval C1 : ",c1," and C2 : ", c2)
f = open("ConfidenceInterval.txt", "a")
f.write("\n C1: {0}s and  C2: {1}s\n".format(c1,c2))



#test_statistic = harmonic_mean

#estimate, bias, stderr, conf_interval = jackknife_stats(data, test_statistic, 0.95)

#print("Standard Deviation ", stderr)

#print("Confidence Interval in jackknife method : ",conf_interval)
