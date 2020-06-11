# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [7.76, 7.81, 7.76, 7.74, 7.83, 7.69, 7.78, 7.46, 7.48, 7.35, 7.5, 7.36, 7.8, 7.59, 7.59, 8.26, 7.72, 8.18, 7.53, 7.66, 7.67, 7.66, 7.74, 7.65, 7.6, 7.66, 7.42, 7.48, 7.51, 7.35]
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