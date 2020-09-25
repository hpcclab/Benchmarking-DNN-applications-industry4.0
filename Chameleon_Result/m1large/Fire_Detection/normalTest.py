# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [21.66, 20.78, 21.41, 21.47, 21.37, 19.88, 21.42, 21.49, 20.58, 21.24, 21.4, 20.8, 21.55, 21.48, 20.56, 21.72, 21.49, 20.5, 20.48, 21.31, 21.47, 21.37, 21.22, 20.94, 20.82, 21.13, 22.03]
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