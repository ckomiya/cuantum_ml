"""
Feature Engineering:
--------------------
Dado el siguiente DataFrame, cree una nueva característica 'D' que sea el producto de 'A', 'B' y 'C':
"""
import pandas as pd


# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [3, 4, 5, 6, 7]
})


#df['D'] = df['A'] * df['B'] * df['C']
df['D'] = df.apply(lambda row: row['A'] * row['B'] * row['C'], axis=1)
print(df)

