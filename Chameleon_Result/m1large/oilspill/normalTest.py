# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [22.13, 22.42, 22.23, 21.89, 28.9, 28.99, 29.11, 23.28, 26.47, 25.27, 23.08, 27.52, 26.78, 25.63, 23.28, 26.54, 26.44, 22.89, 22.36, 22.24, 22.68, 22.38, 22.4, 22.36, 22.03, 22.7, 22.76, 22.5, 22.81, 22.75]
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