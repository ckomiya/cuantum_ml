from sklearn import preprocessing, model_selection, linear_model, metrics




# Create a linear regression model
model = linear_model.LinearRegression()


# Train the model
X = [[0, 0], [1, 1]]
y = [0, 1]
model.fit(X, y)
"""
El método fit() ajusta el modelo a los datos de entrenamiento para encontrar la mejor línea
(o hiperplano en dimensiones más altas) que se ajuste a los datos.
"""

# Make predictions
X_new = [[2, 2]]
y_new = model.predict(X_new)
# se utiliza el método predict() para predecir el valor objetivo correspondiente a la entrada X_new

print(y_new)


# error medio cuadrado
# Calculate the mean squared error of the predictions
y_true = [1]
y_pred = model.predict(X_new)
mse = metrics.mean_squared_error(y_true, y_pred)
print(mse)

"""
El error cuadrático medio (MSE) es una medida de la calidad del ajuste de un modelo de
regresión a los datos observados. Es una medida de la discrepancia entre los valores 
observados (o reales) y los valores predichos por el modelo.
    
"""