import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# Create a StandardScaler
scaler = StandardScaler()

# Perform standardization
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

"""
Al especificar columns=df.columns, estamos asegurando que el nuevo DataFrame
resultante de la estandarización mantenga los mismos nombres de columnas que el 
DataFrame original
"""

print(df_standardized)