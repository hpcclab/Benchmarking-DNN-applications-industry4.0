# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [16.57, 16.52, 16.66, 16.51, 16.56, 16.59, 16.53, 16.63, 16.56, 16.52, 16.53, 16.61, 16.5, 16.6, 16.61, 16.61, 16.6, 16.58, 16.58, 16.61, 16.59, 16.58, 16.58, 16.53, 16.61, 16.54, 16.51, 16.63, 16.6, 16.6]
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
