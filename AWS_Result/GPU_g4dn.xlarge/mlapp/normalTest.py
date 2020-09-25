# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [0.11, 0.1, 0.1, 0.1, 0.11, 0.1, 0.11, 0.11, 0.1, 0.1, 0.1, 0.11, 0.11, 0.1, 0.11, 0.1, 0.11, 0.1, 0.1, 0.1, 0.1, 0.1, 0.11, 0.1, 0.1, 0.1, 0.1, 0.11, 0.1, 0.1]
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
