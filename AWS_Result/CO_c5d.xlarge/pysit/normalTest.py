# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [67.88, 68.15, 67.92, 67.58, 67.8, 67.47, 68.05, 69.12, 68.61, 67.75, 67.76, 68.05, 67.76, 68.06, 67.41, 68.09, 67.26, 67.92, 67.78, 67.98, 67.53, 67.61, 67.34, 68.72, 67.62, 68.03, 67.17, 67.9, 68.74, 67.5]
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
