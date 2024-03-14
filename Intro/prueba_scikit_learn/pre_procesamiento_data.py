from sklearn import preprocessing, model_selection, linear_model, metrics


# StandardScale sirve para estandarizar (normalizar) los datos.

# Create a StandardScaler
scaler = preprocessing.StandardScaler()

"""
Se crea una instancia de la clase StandardScaler, que se utilizará para estandarizar los datos.
StandardScaler aplica una transformación a los datos para que tengan una media de cero y una 
desviación estándar de uno, lo que significa que los datos están centrados alrededor de cero 
y tienen una dispersión uniforme.
"""

# Fit the StandardScaler to the data
data = [[0, 0], [0, 0], [1, 1], [1, 1]]
scaler.fit(data)

"""
Esto calcula la media y la desviación estándar de cada característica en los datos de entrenamiento,
que se utilizarán para estandarizar los datos en el siguiente paso. 
"""

# Transform the data
scaled_data = scaler.transform(data)
print(scaled_data)

"""
Resultado
[[-1. -1.]
 [-1. -1.]
 [ 1.  1.]
 [ 1.  1.]]
 
 cómo se calculó:
 Para cada valor en los datos originales, restamos la media y luego dividimos por la desviación estándar.
 Esto se hace para cada columna de datos.

Para el primer valor en la primera columna: (0 - 0.5) / 0.5 = -1
Para el segundo valor en la primera columna: (0 - 0.5) / 0.5 = -1
Para el tercer valor en la primera columna: (1 - 0.5) / 0.5 = 1
Para el cuarto valor en la primera columna: (1 - 0.5) / 0.5 = 1
Para el primer valor en la segunda columna: (0 - 0.5) / 0.5 = -1
Para el segundo valor en la segunda columna: (0 - 0.5) / 0.5 = -1
Para el tercer valor en la segunda columna: (1 - 0.5) / 0.5 = 1
Para el cuarto valor en la segunda columna: (1 - 0.5) / 0.5 = 1
"""

