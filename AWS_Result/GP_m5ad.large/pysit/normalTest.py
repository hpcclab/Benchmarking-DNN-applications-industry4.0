# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [83.01, 85.08, 82.35, 86.68, 85.24, 84.4, 87.12, 84.38, 84.76, 85.2, 85.65, 82.67, 84.72, 87.09, 85.8, 85.71, 81.85, 85.96, 86.24, 82.35, 86.44, 85.41, 83.73, 87.4, 86.82, 84.01, 86.24, 81.43, 84.32, 84.54]
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
