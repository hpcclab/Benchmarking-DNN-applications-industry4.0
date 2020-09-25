# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [11.74, 11.55, 11.84, 11.73, 11.81, 11.93, 11.89, 11.88, 12.0, 11.67, 11.71, 11.63, 11.82, 11.43, 11.96, 11.6, 11.68, 11.71, 11.73, 11.84, 11.71, 11.75, 11.86, 11.88, 11.91, 12.0, 11.66, 11.9, 11.92, 11.91]
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
