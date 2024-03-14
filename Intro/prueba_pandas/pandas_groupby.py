import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
})

#print(df)
"""
     A      B         C         D
0  foo    one -0.474271 -0.903337
1  bar    one -1.048459  1.627569
2  foo    two -0.537728 -0.090044
3  bar  three  1.049915  0.190919
4  foo    two  0.448746 -0.976683
5  bar    two -3.496795 -1.117209
6  foo    one  0.380383 -0.872139
7  foo  three  0.296793 -1.339610
"""

# Group by column 'A' and calculate the sum of 'C' and 'D' for each group
grouped = df.groupby('A').sum()
print(grouped)
