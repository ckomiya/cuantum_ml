"""
Este código calcula el MSE entre los valores reales y las predicciones, 
lo que proporciona una medida de cuánto difieren las predicciones del 
modelo de los valores reales. Un MSE más bajo indica que las predicciones
del modelo están más cerca de los valores reales, mientras que un MSE 
más alto indica que las predicciones están más lejos de los valores reales.
 
"""

from sklearn.metrics import mean_squared_error

# Datos reales (observados)
y_true = [3, -0.5, 2, 7]

# Predicciones realizadas por el modelo
y_pred = [2.5, 0.0, 2, 8]

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_true, y_pred)

# Imprimir el MSE
print("El error cuadrático medio (MSE) es:", mse)






"""

Un MSE (Error Cuadrático Medio) de 0.375 significa que, en promedio, las predicciones 
del modelo están alejadas de los valores reales por una cantidad de 0.375 unidades al cuadrado.

Para interpretar esto más claramente, ten en cuenta que el MSE es una medida de la discrepancia 
cuadrática entre las predicciones del modelo y los valores reales. Cuando el MSE es más bajo, 
significa que las predicciones del modelo están más cerca de los valores reales, lo que indica
un mejor ajuste del modelo a los datos observados.

En el contexto de tu ejemplo, un MSE de 0.375 sugiere que, en promedio, las predicciones del 
están a una distancia relativamente baja de los valores reales, lo que indica un ajuste 
razonablemente bueno del modelo a los datos. Sin embargo, la interpretación exacta del
MSE puede depender del dominio específico del problema y de las unidades en las que 
expresan los datos.    

el cálculo es al cuadrado por los valores negativos
"""