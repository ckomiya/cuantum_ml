"""
Data Cleaning:
-------------
Dado el siguiente DataFrame, realiza la limpieza de datos llenando los valores faltantes 
con la media de la columna respectiva:
"""


import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan]
})

# Your code here
# Fill missing values with mean of the column
df_filled_mean = df.fillna(df.mean())
print(df_filled_mean)