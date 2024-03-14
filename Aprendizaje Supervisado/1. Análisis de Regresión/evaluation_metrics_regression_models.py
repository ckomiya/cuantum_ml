from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 5, 4, 5]
})

# Create a LinearRegression model
model = LinearRegression()

# Fit the model
model.fit(df[['A']], df['B'])

# Predict new values
predictions = model.predict(df[['A']])
print(predictions)

"""
Error Absoluto Medio (MAE):
---------------------------
Es la media de las diferencias absolutas entre las predicciones y los valores reales.
MAE = Suma de |valor real - predicción| / número de observaciones.
Cuanto menor sea el MAE, mejor será el modelo en términos de precisión.
"""
# Calculate MAE
mae = mean_absolute_error(df['B'], predictions)


"""
Error Cuadrático Medio (MSE):
-----------------------------
Es la media de los cuadrados de las diferencias entre las predicciones y los valores reales.
MSE = Suma de (valor real - predicción)^2 / número de observaciones.
MSE penaliza más fuertemente los errores más grandes que el MAE.
"""
# Calculate MSE
mse = mean_squared_error(df['B'], predictions)


"""
RMSE (Raíz del Error Cuadrático Medio):
---------------------------------------
Es la raíz cuadrada de la media de los cuadrados de las diferencias entre las predicciones y los valores reales.
RMSE = √(MSE)
Proporciona una medida de la dispersión de los errores en la misma escala que los valores originales.
Penaliza más fuertemente los errores grandes que el MAE.
"""
# Calculate RMSE
rmse = np.sqrt(mse)


"""
Coeficiente de Determinación (R-cuadrado o R²):
------------------------------------------------
Es una medida que indica la proporción de la varianza de la variable dependiente que es explicada por el modelo.
R² = 1 - (MSE del modelo / MSE de la línea base).
Toma valores entre 0 y 1, donde 1 indica un ajuste perfecto del modelo y 0 indica que el modelo no explica nada
de la variabilidad de los datos.
Un R² más alto indica un mejor ajuste del modelo a los datos.
"""

# Calculate R-squared
r2 = r2_score(df['B'], predictions)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R-squared:", r2)