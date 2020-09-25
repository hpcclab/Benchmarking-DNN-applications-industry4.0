# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [9.67, 9.9, 9.97, 10.02, 9.94, 9.17, 9.82, 9.12, 9.68, 9.68, 9.52, 9.68, 9.77, 9.54, 9.31, 10.0, 9.64, 9.29, 9.78, 9.79, 9.81, 9.91, 9.63, 10.22, 9.55, 9.55, 10.0, 8.85, 9.96, 9.42]
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
