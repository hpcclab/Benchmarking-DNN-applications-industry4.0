# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [15.98, 15.9, 15.98, 15.98, 15.94, 15.89, 15.97, 15.93, 15.97, 15.87, 15.91, 15.9, 15.95, 15.99, 15.78, 15.86, 15.86, 15.97, 15.96, 15.9, 15.97, 15.9, 15.98, 16.0, 15.98, 15.88, 16.04, 15.91, 15.85, 15.91]
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
