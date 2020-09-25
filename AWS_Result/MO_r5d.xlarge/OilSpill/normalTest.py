# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [17.08, 16.53, 16.46, 16.61, 16.62, 16.56, 16.58, 16.64, 16.53, 16.5, 16.21, 16.3, 16.22, 16.21, 16.23, 16.25, 16.3, 15.91, 15.88, 15.88, 15.96, 16.32, 16.21, 16.34, 16.17, 16.19, 16.27, 16.21, 16.36, 16.31, 16.21]
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
