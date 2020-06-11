# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [8.22, 7.96, 8.73, 8.1, 8.0, 8.88, 8.72, 8.3, 7.88, 8.2, 8.74, 8.45, 8.53, 7.98, 8.38, 8.34, 9.07, 8.21, 7.71, 8.66, 8.15, 8.71, 8.55, 8.56, 9.47, 8.5, 8.64, 8.16, 8.09, 7.87]
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