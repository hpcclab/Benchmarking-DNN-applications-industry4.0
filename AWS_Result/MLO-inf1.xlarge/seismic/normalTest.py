# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [8.64, 8.62, 8.61, 8.65, 8.55, 8.51, 8.6, 8.71, 8.63, 8.66, 8.64, 8.69, 8.59, 8.54, 8.54, 8.57, 8.55, 8.63, 8.71, 8.62, 8.71, 8.65, 8.68, 8.95, 8.62, 8.61, 8.68, 8.54, 8.55, 8.65]
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
