import numpy as np
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats
from statistics import harmonic_mean
import math

#data = np.array([1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40])
data = np.array([1.592783505154639, 1.5825864276568502, 1.592783505154639, 1.5968992248062015, 1.578544061302682, 1.6072821846553964, 1.588688946015424, 1.6568364611260054, 1.6524064171122992, 1.6816326530612244, 1.648, 1.6793478260869563, 1.5846153846153845, 1.6284584980237153, 1.6284584980237153, 1.4963680387409202, 1.6010362694300517, 1.511002444987775, 1.641434262948207, 1.6135770234986944, 1.6114732724902217, 1.6135770234986944, 1.5968992248062015, 1.6156862745098037, 1.6263157894736842, 1.6135770234986944, 1.6657681940700808, 1.6524064171122992, 1.6458055925432755, 1.6816326530612244])

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
