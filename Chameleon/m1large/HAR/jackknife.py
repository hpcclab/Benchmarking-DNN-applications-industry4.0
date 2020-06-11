import numpy as np
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats
from statistics import harmonic_mean
import math

#data = np.array([1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40])
data = np.array([1.1423290203327172, 1.2249752229930624, 1.1693472090823083, 1.220138203356367, 1.2625127681307458, 1.2035053554040895, 1.2716049382716048, 1.129798903107861, 1.2888425443169969, 1.2955974842767297, 1.2848232848232848, 1.1704545454545454, 1.1605633802816901, 1.2237623762376237, 1.197674418604651, 1.294240837696335, 1.2650972364380757, 1.2888425443169969, 1.3010526315789472, 1.2129538763493621, 1.3051742344244983, 1.1095152603231597, 1.1339449541284403, 1.243460764587525, 1.2035053554040895, 1.2310756972111554, 1.105545617173524, 1.0189612530915086, 1.2347652347652347, 1.1884615384615385])

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
