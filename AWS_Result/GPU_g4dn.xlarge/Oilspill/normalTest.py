# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [7.88, 7.93, 7.95, 7.97, 8.01, 8.1, 7.99, 7.98, 8.13, 8.09, 8.09, 8.12, 8.13, 8.14, 8.13, 8.13, 8.12, 8.15, 8.08, 8.12, 8.1, 8.15, 8.13, 8.13, 8.19, 8.18, 8.13, 8.13, 8.19, 8.16]
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
