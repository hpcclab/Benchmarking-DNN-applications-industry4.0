# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [71.69, 71.28, 70.96, 71.96, 71.39, 71.09, 71.53, 71.93, 71.44, 71.77, 71.21, 71.31, 71.37, 71.36, 70.99, 72.28, 71.4, 72.48, 73.28, 73.21, 72.88, 71.48, 71.91, 71.41, 72.73, 72.82, 71.39, 72.16, 74.28, 77.95]
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
