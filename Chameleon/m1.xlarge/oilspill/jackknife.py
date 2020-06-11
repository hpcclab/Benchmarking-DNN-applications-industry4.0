import numpy as np
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats
from statistics import harmonic_mean
import math

#data = np.array([1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40])
data = np.array([247.28729281767957, 246.6060606060606, 240.8556053811659, 243.03529411764703, 243.47597461468723, 243.03529411764703, 243.25543478260872, 247.74354243542436, 248.6611111111111, 247.0597976080957, 248.43108233117482, 246.37981651376145, 243.03529411764703, 243.47597461468723, 241.50539568345326, 245.70356816102472, 245.92857142857142, 246.6060606060606, 246.153987167736, 245.25479452054796, 245.25479452054796, 247.28729281767957, 242.5962059620596, 247.5152073732719, 247.74354243542436, 246.6060606060606, 247.28729281767957, 243.47597461468723, 243.47597461468723, 245.47897623400365])

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
