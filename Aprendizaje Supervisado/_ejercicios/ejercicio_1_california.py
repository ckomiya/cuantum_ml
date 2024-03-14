"""
Utilizando el conjunto de datos de California disponible en Scikit-learn, 
realiza un análisis de regresión lineal simple para predecir el valor mediano de las viviendas
ocupadas por sus propietarios. Evalúe su modelo utilizando las métricas MAE, MSE, RMSE y R cuadrado.
"""

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd

# Load the California housing dataset
california = fetch_california_housing(as_frame=True)

# Create a DataFrame
df = california.frame

print("\nCalifornia Frame")
print(california.frame)
print("\nCalifornia Target")
print(california.target)

# Create a LinearRegression model
model = LinearRegression()

# Fit the model
model.fit(df[['MedInc']], california.target)

# Predict new values
predictions = model.predict(df[['MedInc']])

# Calculate metrics
mae = mean_absolute_error(california.target, predictions)
mse = mean_squared_error(california.target, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(california.target, predictions)
print("\nMétricas de Evaluación:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R-squared:", r2)
