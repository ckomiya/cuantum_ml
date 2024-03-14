from sklearn.preprocessing import MinMaxScaler
import pandas as pd


# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
})

# Create a MinMaxScaler
scaler = MinMaxScaler()
"""
MinMaxScaler es una técnica de escalado que transforma los datos para que estén en un rango específico,
generalmente entre 0 y 1.
"""

# Perform normalization
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
"""
Se llama al método fit_transform() del objeto scaler para realizar la normalización en el DataFrame df. 
Este método ajusta el escalador al DataFrame y transforma los datos. En este caso, se normalizan
las columnas de df. El resultado es un array NumPy con los datos normalizados.

Se crea un nuevo DataFrame df_normalized utilizando el array NumPy obtenido en el paso anterior.
Se establecen las mismas columnas que df para mantener la estructura de datos.
"""
print(df_normalized)