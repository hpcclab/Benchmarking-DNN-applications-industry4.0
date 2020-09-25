# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [10.82, 10.09, 10.57, 10.13, 9.79, 10.27, 9.72, 10.94, 9.59, 9.54, 9.62, 10.56, 10.65, 10.1, 10.32, 9.55, 9.77, 9.59, 9.5, 10.19, 9.47, 11.14, 10.9, 9.94, 10.27, 10.04, 11.18, 12.13, 10.01, 10.4]
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