import numpy as np
import pandas as pd
from numpy.random import randn


df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['X', 'Y', 'Z', 'W'])


print("Original DataFrame:\n", df)

df['new index'] = df['W'] + df['Y']
print("\nDataFrame after adding 'new index':\n", df)

df = df.drop('new index', axis=1)
print("\nDataFrame after dropping 'new index':\n", df)


print("\nRow 'C' using loc:\n", df.loc['C'])


print("\nRow at index 2 using iloc:\n", df.iloc[2])


print("\nTable which contains values true or false greater than 0:\n",df>0)

print("\nColumn which has elements greater than 0:\n",df['Y']>0)

print("\nColumn which has elements less than 0:\n",df['Z']<0)

print("\nMore than one condition:\n",df[(df['X']>0) | (df['Z']<0)])

print("\nMore than one condition:\n",df[(df['X']>0) & (df['Z']<0)])

newcol='pak ind turkey switzerland  usa'.split()

df['States']=newcol

print(df['States'])

