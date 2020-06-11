# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [10.18, 9.68, 9.78, 9.36, 9.19, 9.4, 9.36, 8.81, 8.74, 9.22, 10.54, 9.57, 10.04, 9.75, 9.66, 9.59, 9.15, 8.9, 9.43, 9.38, 9.93, 9.72, 8.92, 10.06, 8.96, 9.74, 9.79, 9.52, 9.3, 9.74]
stat, p = shapiro(data)
print('stat=%.3f, p=%.3f' % (stat, p))
f = open("NormalTestShapiro-Wilk.txt", "a")

if p > 0.05:
	print('Probably Gaussian')
	f.write('Probably Gaussian\n')
else:
	print('Probably not Gaussian')
	f.write('Probably not Gaussian\n')

f.write("Stat: {0}s and  p: {1}s\n".format(stat,p))

f.close()
