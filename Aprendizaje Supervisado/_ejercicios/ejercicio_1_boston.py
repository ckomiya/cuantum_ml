"""
Utilizando el conjunto de datos de Boston disponible en Scikit-learn, 
realiza un análisis de regresión lineal simple para predecir el valor mediano de las viviendas
ocupadas por sus propietarios. Evalúe su modelo utilizando las métricas MAE, MSE, RMSE y R cuadrado.
"""

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd

# Load the Boston Housing dataset
boston = load_boston()

# Create a DataFrame
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target

# Create a LinearRegression model
model = LinearRegression()

# Fit the model
model.fit(df[['RM']], df['MEDV'])

# Predict new values
predictions = model.predict(df[['RM']])

# Calculate metrics
mae = mean_absolute_error(df['MEDV'], predictions)
mse = mean_squared_error(df['MEDV'], predictions)
rmse = np.sqrt(mse)
r2 = r2_score(df['MEDV'], predictions)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R-squared:", r2)