# D'Agostino and Pearson's Test
from numpy.random import seed
from numpy.random import randn
from scipy.stats import normaltest
# seed the random number generator
seed(1)
# generate univariate observations
#data = 5 * randn(100) + 50
data = [11.5, 12.6, 11.12, 11.69, 10.82, 10.79, 10.98, 11.09, 11.37, 11.46, 11.92, 11.15, 11.0, 11.14, 11.91, 11.44, 10.83, 12.49, 10.78, 10.9, 11.63, 11.08, 15.59, 10.77, 13.02, 11.29, 10.67, 10.4, 10.68, 11.45]
# normality test
stat, p = normaltest(data)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')



# Anderson-Darling Test
from numpy.random import seed
from numpy.random import randn
from scipy.stats import anderson
# seed the random number generator
seed(1)
# generate univariate observations
#data = 5 * randn(100) + 50
# normality test
result = anderson(data)
print('Statistic: %.3f' % result.statistic)
p = 0
for i in range(len(result.critical_values)):
	sl, cv = result.significance_level[i], result.critical_values[i]
	if result.statistic < result.critical_values[i]:
		print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
	else:
		print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))


# QQ Plot
from numpy.random import seed
from numpy.random import randn
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
# seed the random number generator
#seed(1)
# generate univariate observations
#data = 5 * randn(100) + 50
# q-q plot
qqplot(data, line='s')
pyplot.show()