# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [64.88, 64.9, 64.89, 65.12, 64.75, 64.71, 64.9, 65.1, 64.75, 64.68, 64.29, 64.33, 64.91, 65.09, 65.02, 64.91, 64.95, 64.68, 65.07, 64.98, 64.47, 64.74, 64.61, 65.21, 64.74, 64.91, 64.31, 64.98, 64.55, 64.82]
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
