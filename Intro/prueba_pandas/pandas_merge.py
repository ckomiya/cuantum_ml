import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key': ['K0', 'K1', 'K0', 'K1']
})
#print(df1)

"""
    A   B key
0  A0  B0  K0
1  A1  B1  K1
2  A2  B2  K0
3  A3  B3  K1
"""

df2 = pd.DataFrame({
    'C': ['C0', 'C1'],
    'D': ['D0', 'D1']},
    index=['K0', 'K1']
)
#print(df2)
"""
     C   D
K0  C0  D0
K1  C1  D1
"""



# Merge df1 and df2 on the 'key' column
merged = pd.merge(df1, df2, left_on='key', right_index=True)
# left_on='key': Especifica que la columna 'key' en df1 será utilizada como clave de fusión.
# right_index=True: Indica que los índices de df2 se utilizarán como claves de fusión.
print(merged)

