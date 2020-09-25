# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [16.25, 16.5, 16.47, 15.96, 16.01, 16.75, 15.63, 16.2, 16.0, 16.57, 16.38, 15.89, 16.23, 16.15, 16.8, 16.41, 15.78, 16.23, 15.92, 16.58, 16.33, 15.49, 16.23, 16.65, 16.8, 16.41, 15.78, 16.53, 15.96]
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