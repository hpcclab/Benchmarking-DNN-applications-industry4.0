# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [13.83, 14.47, 14.03, 15.46, 15.61, 13.6, 15.26, 14.13, 14.41, 13.7, 14.23, 14.49, 14.0, 13.73, 13.92, 13.82, 13.81, 13.88, 13.71, 14.08, 14.1, 13.38, 13.69, 13.56, 13.57, 13.63, 13.59, 13.64, 13.97, 13.29, 13.72]
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
