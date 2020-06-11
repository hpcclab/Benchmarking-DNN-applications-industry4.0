import numpy as np
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats
from statistics import harmonic_mean
import math

#data = np.array([1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40])
data = np.array([123.06614785992218, 118.06999533364441, 117.3036624942049, 122.47047434656339, 123.6676441837732, 123.72811735941319, 122.11583011583011, 123.97060264576187, 119.74633222905821, 122.76758854924793, 128.0485829959514, 125.50793650793649, 118.06999533364441, 122.88683827100533, 122.64857004362578, 118.12511671335199, 107.89936034115138, 122.11583011583011, 123.84924131179636, 119.74633222905821, 122.76758854924793, 128.0485829959514, 117.57620817843865, 123.84924131179636, 119.74633222905821, 122.76758854924793, 128.0485829959514, 119.63309692671395, 128.7653944020356, 128.2432843385707])

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


t = 2.052

c1 = harmonica - ((t*std)/math.sqrt(n))

c2 = harmonica + ((t*std)/math.sqrt(n))

print(" Confidence interval C1 : ",c1," and C2 : ", c2)
f = open("ConfidenceInterval.txt", "a")
f.write("\n C1: {0}s and  C2: {1}s\n".format(c1,c2))



#test_statistic = harmonic_mean

#estimate, bias, stderr, conf_interval = jackknife_stats(data, test_statistic, 0.95)

#print("Standard Deviation ", stderr)

#print("Confidence Interval in jackknife method : ",conf_interval)
