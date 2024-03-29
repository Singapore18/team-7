from analyze import processData

import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import operator


data2 = "test2.csv"
df = pd.read_csv(data2)
df = df.dropna(axis=1)
df.head()


dataArray = df.values
resultArray = []

types = ['growth', 'confidence', 'strategic', 'productive', 'team']

typeDict = {}
for type in types:
    typeDict[type] = 0

for data in dataArray:

    datadict = {}
    for index, value in enumerate(data):
        datadict[index+1] = value
    result = processData(datadict,collaborate = False)

    for type in types:
        typeDict[type] += result[type]

for type in types:
    typeDict[type] = typeDict[type]/len(dataArray)

print(typeDict)
