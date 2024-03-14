from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Create a list of categories
categories = [['red'], ['blue'], ['green'], ['red'], ['green'], ['blue'], ['blue'], ['green']]


df = pd.DataFrame(categories)
print(df)
"""
       0
0    red
1   blue
2  green
3    red
4  green
5   blue
6   blue
7  green
"""

# Create a OneHotEncoder
#encoder = OneHotEncoder(sparse=False)
encoder = OneHotEncoder()

# Perform One-Hot Encoding
onehot_encoded_categories = encoder.fit_transform(categories)

print(onehot_encoded_categories)

"""
 Cuando aplicas el one-hot encoding utilizando fit_transform() en un DataFrame,
 el resultado que obtienes son solo los valores que tienen el indicador "1.0",
 ya que el one-hot encoding elimina la redundancia y solo muestra los valores presentes.
 
El "1.0" en el output indica que la categoría correspondiente está presente para la 
observación asociada. Es decir, si en una fila específica del DataFrame original, 
una categoría está presente en una columna categórica dada, se representará como un 
"1.0" en la posición correspondiente en la matriz dispersa generada por el one-hot
encoding. Por lo tanto, cada "1.0" indica la presencia de una categoría específica
para una observación particular. Si no está presente, se representaría como un "0.0".
"""


