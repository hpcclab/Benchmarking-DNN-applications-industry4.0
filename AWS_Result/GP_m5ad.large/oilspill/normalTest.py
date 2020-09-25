# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [130.63, 130.86, 130.85, 130.62, 130.87, 130.52, 131.17, 130.63, 132.51, 130.85, 130.63, 130.79, 130.49, 130.76, 130.72, 131.02, 130.85, 130.52, 130.77, 130.48, 130.68, 130.83, 131.08, 130.72, 130.66, 130.77, 130.61, 130.69, 139.44, 135.7]
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
