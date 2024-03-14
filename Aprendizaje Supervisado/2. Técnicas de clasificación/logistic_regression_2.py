import pandas as pd
from sklearn.linear_model import LogisticRegression


"""
Escenario más realista:
Podemos usar un conjunto de datos ficticio que muestre la relación
entre la edad de las personas y si tienen o no diabetes. Aquí tienes un ejemplo:
"""
# Crear un DataFrame
df = pd.DataFrame({
    'Edad': [25, 35, 45, 55, 65, 75, 85],
    'Diabetes': [0, 0, 1, 0, 1, 1, 1]
})

# Crear un modelo de regresión logística
modelo = LogisticRegression()

# Ajustar el modelo
modelo.fit(df[['Edad']], df['Diabetes'])

# Predecir nuevos valores
predicciones = modelo.predict(df[['Edad']])

print(predicciones)