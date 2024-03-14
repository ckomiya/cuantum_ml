from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Crear un DataFrame
df = pd.DataFrame({
    'Peso': [100, 150, 200, 250, 300],
    'Textura': ['rugosa', 'rugosa', 'suave', 'suave', 'rugosa'],
    'Fruta': ['manzana', 'manzana', 'naranja', 'naranja', 'manzana']
})

# Codificar la textura como valores numéricos
df['Textura'] = df['Textura'].map({'rugosa': 0, 'suave': 1})
print(df)
# Crear un modelo de árbol de decisión
modelo = DecisionTreeClassifier()

# Ajustar el modelo
modelo.fit(df[['Peso', 'Textura']], df['Fruta'])

# Predecir nuevas frutas
pesos_nuevos = [180, 220]
texturas_nuevas = [0, 1]
nuevas_frutas = modelo.predict(pd.DataFrame({'Peso': pesos_nuevos, 'Textura': texturas_nuevas}))

print(nuevas_frutas)