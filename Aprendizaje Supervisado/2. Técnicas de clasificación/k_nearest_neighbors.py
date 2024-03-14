from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [0, 0, 0, 1, 1]
})

# Create a KNN Classifier
model = KNeighborsClassifier(n_neighbors=3)
"""
 n_neighbors determina cuántos vecinos se considerarán al clasificar un punto de datos
 desconocido utilizando el algoritmo k-NN. Un valor adecuado para este parámetro depende 
 de la naturaleza del problema y se selecciona mediante técnicas de validación
 cruzada u otras estrategias de ajuste de hiperparámetros.
"""

# Train the model using the training sets
model.fit(df[['A']], df['B'])

# Predict the response for test dataset
y_pred = model.predict(df[['A']])

print(y_pred)