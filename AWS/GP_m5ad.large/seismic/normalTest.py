# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [14.29, 14.15, 14.24, 14.25, 14.3, 14.36, 14.26, 14.32, 14.33, 14.14, 13.97, 14.3, 14.18, 14.21, 14.6, 14.4, 14.4, 14.37, 14.37, 14.18, 14.45, 14.23, 14.19, 14.12, 14.52, 14.38, 14.33, 14.52, 14.31, 14.23]
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
