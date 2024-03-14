import pandas as pd


df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
})

"""
   A  B
0  1  a
1  2  b
2  3  c
"""

# Select a column
#print(df['A'])  #<class 'pandas.core.series.Series'>


# Select multiple columns
#print(df[['A', 'B']])

# Select a row by label (etiqueta de fila)
#print(df.loc[0])

# Select a row by number
#print(df.iloc[0])

# Select a specific value
print(df.loc[0, 'A'])   # devuelve 1
print(df.iloc[0, 0])    # devuelve 1
