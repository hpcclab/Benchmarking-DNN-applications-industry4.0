# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [11.43, 11.74, 11.59, 11.49, 11.47, 11.44, 11.65, 11.46, 11.56, 11.42, 11.42, 11.45, 11.67, 11.43, 11.46, 11.51, 11.61, 11.45, 11.45, 11.5, 11.65, 11.57, 11.44, 11.49, 11.48, 11.48, 11.68, 11.47, 11.45, 11.65]
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
