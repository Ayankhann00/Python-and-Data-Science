import numpy as np
import pandas as pd
from numpy.random import randn
#multi indexing in Data Frames

l1 = ['G1', 'G1', 'G1', 'G2', 'G2']
l2 = [0, 1, 2, 0, 1]
multi_index = list(zip(l1, l2))
multi_index = pd.MultiIndex.from_tuples(multi_index)

df = pd.DataFrame(randn(5, 4), index=multi_index, columns=['A', 'B', 'C', 'D'])

print(df)

#get elements of G1 row
print(df.loc['G1'])

#get elements of G2 row
print(df.loc['G2'])

#get elements of G2 of 2 column

print(df.loc['G2'].loc[1])

#naming the indexes

df.index.names=['Groups','Values']

print(df)


#grab the value from an index directly

print(df.xs(1,level="Values"))
