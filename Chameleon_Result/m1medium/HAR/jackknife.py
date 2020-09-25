import numpy as np
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats
from statistics import harmonic_mean
import math

#data = np.array([1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40])
data = np.array([1.503649635036496, 1.5527638190954773, 1.415807560137457, 1.525925925925926, 1.545, 1.3918918918918917, 1.4174311926605503, 1.4891566265060239, 1.5685279187817258, 1.5073170731707317, 1.4141876430205949, 1.4627218934911244, 1.4490035169988278, 1.5488721804511276, 1.474940334128878, 1.4820143884892085, 1.362734288864388, 1.5054811205846526, 1.603112840466926, 1.4272517321016165, 1.516564417177914, 1.4190585533869113, 1.4456140350877191, 1.4439252336448596, 1.3051742344244983, 1.4541176470588235, 1.4305555555555554, 1.5147058823529411, 1.5278121137206426, 1.570520965692503])

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
