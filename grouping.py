import numpy as np
import pandas as pd
from numpy.random import randn

# Group By and agregate functions in pandas

d={'Company':['Amazon','Amazon','Instagram','Instagram','Google','Linkedin'],'Users':['Ayan','Hamza','Shees','Safwan','Ahmed','Ali'],'Sales':[0,100,200,300,500,350]}

df=pd.DataFrame(d)



agregate=df.groupby('Company')['Sales']

print(agregate.sum())

print(agregate.mean())

#groupby all methods 

print(agregate.describe())
print(agregate.describe().transpose())['Amazon']
#groupby standard deviation

print(agregate.std())

