import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

sns.set(color_codes=True)

#x = np.random.normal(size=100)

data = [11.5, 12.6, 11.12, 11.69, 10.82, 10.79, 10.98, 11.09, 11.37, 11.46, 11.92, 11.15, 11.0, 11.14, 11.91, 11.44, 10.83, 12.49, 10.78, 10.9, 11.63, 11.08, 15.59, 10.77, 13.02, 11.29, 10.67, 10.4, 10.68, 11.45]
sns.distplot(data);