# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [9.64, 9.73, 9.77, 9.69, 9.71, 9.81, 9.79, 9.84, 9.6, 9.75, 9.7, 9.67, 9.66, 9.69, 9.8, 9.67, 9.66, 9.66, 9.79, 9.61, 9.64, 9.68, 9.59, 9.69, 9.68, 9.67, 9.73, 9.75, 9.73, 9.74]
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
