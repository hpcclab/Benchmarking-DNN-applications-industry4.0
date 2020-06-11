# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [20.56, 21.43, 21.57, 20.66, 20.46, 20.45, 20.72, 20.41, 21.13, 20.61, 19.76, 20.16, 21.43, 20.59, 20.63, 21.42, 23.45, 20.72, 20.43, 21.13, 20.61, 19.76, 21.52, 20.43, 21.13, 20.61, 19.76, 21.15, 19.65, 19.73]
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