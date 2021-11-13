from typing import Union, Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import ndarray
from pandas import Series, DataFrame
from pandas.core.arrays import ExtensionArray
from pandas.core.generic import NDFrame
from pylab import rcParams
import seaborn as sb
import scipy
from scipy.stats import pearsonr


rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

addresses = r'C:\Users\jvalasek001\Desktop\PyCode\Statistics\Data\mtcars.csv'
cars = pd.read_csv(addresses)
cars.columns = ['names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg: Union[Union[Series, ExtensionArray, None, ndarray, DataFrame, NDFrame], Any] = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
vs = cars['vs']

pCor, pValue = pearsonr(mpg, hp)
print(round(pCor, 3))   
print(min(mpg))

dfX = cars[['mpg', 'hp', 'qsec', 'vs']]
corr = dfX.corr((method ='pearson'))
corr2 =dfX.corr((method ='kendall'))
corr3 = dfX.corr((method ='spearman'))

print(corr)
print(corr2)
print(corr3)


# Plot
plt.scatter(mpg, hp)
plt.xlabel('MPG')
plt.ylabel('HP')
plt.title('MPG vs HP')
plt.show()
#TODO: Add a correlation matrix



