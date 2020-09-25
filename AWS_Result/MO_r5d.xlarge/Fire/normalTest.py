# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [12.16, 12.16, 12.09, 12.23, 12.04, 12.15, 12.18, 11.98, 12.12, 11.02, 12.04, 12.2, 11.88, 11.8, 12.0, 12.33, 12.23, 12.32, 12.38, 12.22, 12.23, 12.4, 12.22, 12.49, 12.08, 12.14, 12.52, 12.57, 12.6, 12.26]
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
