# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [71.4, 70.97, 71.36, 71.25, 71.58, 70.65, 70.69, 71.12, 71.3, 71.01, 70.97, 71.28, 71.63, 71.13, 71.62, 71.18, 71.7, 70.88, 70.91, 71.03, 71.04, 70.99, 70.9, 71.84, 70.81, 71.36, 71.39, 71.31, 71.27, 71.49]
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
