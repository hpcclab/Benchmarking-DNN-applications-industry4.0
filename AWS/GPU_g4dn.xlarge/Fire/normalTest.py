# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [4.65, 4.67, 4.68, 4.67, 4.7, 4.61, 4.68, 4.68, 4.7, 4.66, 4.7, 4.62, 4.63, 4.7, 4.7, 4.65, 4.71, 4.71, 4.66, 4.71, 4.71, 4.69, 4.69, 4.73, 4.62, 4.67, 4.69, 4.68, 4.61, 4.62]
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
