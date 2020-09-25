import numpy as np
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats
from statistics import harmonic_mean
import math

#data = np.array([1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40])
data = np.array([1.0747826086956522, 0.9809523809523809, 1.1115107913669064, 1.0573139435414884, 1.1423290203327172, 1.1455050973123262, 1.1256830601092895, 1.1145175834084762, 1.087071240105541, 1.0785340314136125, 1.0369127516778522, 1.1085201793721973, 1.1236363636363635, 1.1095152603231597, 1.0377833753148613, 1.0804195804195804, 1.1412742382271468, 0.9895916733386709, 1.1465677179962894, 1.1339449541284403, 1.0627687016337057, 1.115523465703971, 0.7928159076330981, 1.1476323119777159, 0.9493087557603687, 1.0947741364038972, 1.1583880037488286, 1.1884615384615385, 1.1573033707865168, 1.0794759825327511 ])

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
