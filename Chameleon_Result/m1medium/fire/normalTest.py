# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [29.64, 21.2, 21.48, 20.57, 20.74, 20.19, 20.17, 20.54, 20.1, 20.21, 20.51, 20.41, 20.48, 20.08, 19.5, 20.81, 20.79, 18.39, 19.43, 20.67, 20.87, 20.41, 19.87, 20.61, 20.31, 20.53, 20.85, 20.16, 18.02, 19.34]
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