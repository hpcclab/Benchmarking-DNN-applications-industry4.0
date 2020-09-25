# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [11.51, 10.09, 9.89, 9.99, 9.76, 10.14, 10.06, 10.29, 10.02, 9.74, 10.54, 9.91, 10.04, 9.71, 10.09, 10.79, 10.34, 11.79, 10.21, 9.99, 10.07, 9.96, 10.34, 10.15, 9.95, 9.85, 10.16, 9.98, 9.94, 10.24]
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
