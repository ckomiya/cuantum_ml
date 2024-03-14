from sklearn.linear_model import LinearRegression

"""
Supongamos que tienes un modelo de regresión lineal entrenado para predecir
el precio de una casa en función de su tamaño (en pies cuadrados). Después
de entrenar el modelo, deseas usarlo para predecir el precio de una casa
nueva que tiene un tamaño de 1500 pies cuadrados.
"""

# Supongamos que tienes datos de entrenamiento X_train, y los correspondientes precios de las casas y_train
# Datos de entrenamiento (tamaño de la casa en pies cuadrados)
X_train = [[1000], [1500], [2000], [2500], [3000]]
# Precios correspondientes de las casas
y_train = [150000, 200000, 250000, 300000, 350000]

# Entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Tamaño de la casa para la que quieres hacer una predicción (en este caso, 1500 pies cuadrados)
house_size = [[1500]]

# Hacer la predicción utilizando el modelo entrenado
predicted_price = model.predict(house_size)

# Imprimir la predicción
print("El precio predicho de la casa es:", predicted_price)