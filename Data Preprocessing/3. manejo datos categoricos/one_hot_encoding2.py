import pandas as pd

# Creamos el DataFrame original
data = {
    'Color': ['Rojo', 'Azul', 'Verde', 'Rojo', 'Verde', 'Azul', 'Azul', 'Verde'],
    'Tamaño': ['Grande', 'Pequeño', 'Mediano', 'Mediano', 'Grande', 'Pequeño', 'Grande', 'Mediano'],
    'Forma': ['Círculo', 'Triángulo', 'Círculo', 'Triángulo', 'Cuadrado', 'Círculo', 'Cuadrado', 'Triángulo']
}

df = pd.DataFrame(data)
print(df)
"""
   Color   Tamaño      Forma
0    Rojo   Grande    Círculo
1    Azul  Pequeño  Triángulo
2   Verde  Mediano    Círculo
3    Rojo  Mediano  Triángulo
4   Verde   Grande   Cuadrado
5    Azul  Pequeño    Círculo
6    Azul   Grande   Cuadrado
7   Verde  Mediano  Triángulo
"""



from sklearn.preprocessing import OneHotEncoder

# Creamos el codificador OneHotEncoder
encoder = OneHotEncoder()

# Realizamos el One-Hot Encoding
onehot_encoded_categories = encoder.fit_transform(df)

print(onehot_encoded_categories)
"""
(0, 0)    1.0   # La primera fila (índice 0) tiene la categoría 'Rojo' en la columna 'Color'
(1, 2)    1.0   # La segunda fila (índice 1) tiene la categoría 'Azul' en la columna 'Color'
(2, 3)    1.0   # La tercera fila (índice 2) tiene la categoría 'Verde' en la columna 'Color'
(3, 0)    1.0   # La cuarta fila (índice 3) tiene la categoría 'Rojo' en la columna 'Color'
(4, 3)    1.0   # La quinta fila (índice 4) tiene la categoría 'Verde' en la columna 'Color'
(5, 2)    1.0   # La sexta fila (índice 5) tiene la categoría 'Azul' en la columna 'Color'
(6, 2)    1.0   # La séptima fila (índice 6) tiene la categoría 'Azul' en la columna 'Color'
(7, 3)    1.0   # La octava fila (índice 7) tiene la categoría 'Verde' en la columna 'Color'
(0, 4)    1.0   # La primera fila (índice 0) tiene la categoría 'Grande' en la columna 'Tamaño'
(1, 1)    1.0   # La segunda fila (índice 1) tiene la categoría 'Pequeño' en la columna 'Tamaño'
(2, 2)    1.0   # La tercera fila (índice 2) tiene la categoría 'Mediano' en la columna 'Tamaño'
(3, 2)    1.0   # La cuarta fila (índice 3) tiene la categoría 'Mediano' en la columna 'Tamaño'
(4, 4)    1.0   # La quinta fila (índice 4) tiene la categoría 'Grande' en la columna 'Tamaño'
(5, 1)    1.0   # La sexta fila (índice 5) tiene la categoría 'Pequeño' en la columna 'Tamaño'
(6, 4)    1.0   # La séptima fila (índice 6) tiene la categoría 'Grande' en la columna 'Tamaño'
(7, 2)    1.0   # La octava fila (índice 7) tiene la categoría 'Mediano' en la columna 'Tamaño'
(0, 5)    1.0   # La primera fila (índice 0) tiene la categoría 'Círculo' en la columna 'Forma'
(1, 6)    1.0   # La segunda fila (índice 1) tiene la categoría 'Triángulo' en la columna 'Forma'
(2, 5)    1.0   # La tercera fila (índice 2) tiene la categoría 'Círculo' en la columna 'Forma'
(3, 6)    1.0   # La cuarta fila (índice 3) tiene la categoría 'Triángulo' en la columna 'Forma'
(4, 7)    1.0   # La quinta fila (índice 4) tiene la categoría 'Cuadrado' en la columna 'Forma'
(5, 5)    1.0   # La sexta fila (índice 5) tiene la categoría 'Círculo' en la columna 'Forma'
(6, 7)    1.0   # La séptima fila (índice 6) tiene la categoría 'Cuadrado' en la columna 'Forma'
(7, 6)    1.0   # La octava fila (índice 7) tiene la categoría 'Triángulo' en la columna 'Forma'
"""