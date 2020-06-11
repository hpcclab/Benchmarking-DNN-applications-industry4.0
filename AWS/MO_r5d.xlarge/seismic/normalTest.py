# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [10.7, 10.72, 10.75, 10.73, 10.69, 10.74, 10.68, 10.72, 10.67, 10.78, 10.69, 10.77, 10.62, 10.68, 10.79, 10.73, 10.79, 10.69, 10.78, 10.73, 10.79, 10.65, 10.8, 10.55, 10.72, 10.69, 10.39, 10.46, 10.66, 10.45]
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
