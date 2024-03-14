import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': ['a', 'b', 'c'],
})

"""
numpy.nan es una constante especial en NumPy que representa un valor "no un número" 
(NaN por sus siglas en inglés: "Not a Number"). 
Se utiliza para indicar la ausencia de un valor numérico o para representar
resultados indefinidos o no válidos en cálculos numéricos.
"""

# Fill missing values
df_filled = df.fillna(0)
#print(df_filled)


# Replace values
df_replaced = df.replace(np.nan, 0)
print(df_replaced)

