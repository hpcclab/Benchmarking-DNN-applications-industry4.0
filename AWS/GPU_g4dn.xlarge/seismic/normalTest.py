# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [10.48, 10.2, 10.27, 10.33, 10.44, 10.4, 10.21, 10.32, 10.44, 10.32, 10.51, 10.31, 10.45, 10.27, 10.32, 10.41, 10.39, 10.36, 10.28, 10.33, 10.43, 10.24, 10.33, 10.45, 10.35, 10.24, 10.34, 10.46, 10.38, 10.38]
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
