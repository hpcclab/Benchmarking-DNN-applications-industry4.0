# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [10.86, 10.89, 11.15, 11.05, 11.03, 11.05, 11.04, 10.84, 10.8, 10.87, 10.81, 10.9, 11.05, 11.03, 11.12, 10.93, 10.92, 10.89, 10.91, 10.95, 10.95, 10.86, 11.07, 10.85, 10.84, 10.89, 10.86, 11.03, 11.03, 10.94]
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