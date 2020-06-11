# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [11.2, 11.28, 11.24, 11.22, 11.31, 11.39, 11.5, 11.6, 11.61, 11.58, 11.62, 11.54, 11.6, 11.64, 11.6, 11.69, 11.65, 11.74, 11.31, 11.3, 11.27, 11.29, 11.26, 11.31, 11.33, 11.38, 11.4, 11.33, 11.6, 12.08, 11.9]
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
