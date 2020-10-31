#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

# Data Filtering Example
from numpy import nan as NA

print()
print('Example 1')

print()
print('b4')
data = pd.Series([2, 2.5, NA, 4, NA, 8])
print(data)

# drops the NAs
data.dropna()

# creates a panda series of all non-NA values
s = data[data.notnull()]
print()
print(s)

print()
print('Example 2')
# builds another data frame
data = pd.DataFrame([[2., 8.5, 5.], [1., NA, NA],
                     [NA, NA, NA], [NA, 8.5, 5.]])
print()
print('b4')
print(data)

data.dropna(how='all')
data[4] = NA

# drops rows(s) with all values missing
t=data.dropna(axis=0, how='all')
print()
print('after')
print(t)

print()
print('Example 3')
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print()
print('initial data set')
print(data)

df.dropna()

# Keep the rows with at least 2 non-NA values
df.dropna(thresh=2)
print()
print('after transformation')
print(df)

