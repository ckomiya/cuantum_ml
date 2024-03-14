"""
Data Scaling and Normalization
-------------------------------

Dado el siguiente DataFrame, realice la estandarización de todas las características:
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

# Create a StandardScaler
scaler = StandardScaler()

# Perform standardization
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print(df_standardized)