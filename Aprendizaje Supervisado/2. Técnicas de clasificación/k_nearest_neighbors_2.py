from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Definir los datos de entrenamiento
X_train = np.array([[1, 2], [2, 3], [3, 4], [5, 1], [6, 2]])
y_train = np.array(['A', 'A', 'B', 'B', 'B'])

# Crear el clasificador KNeighbors con 3 vecinos
clf = KNeighborsClassifier(n_neighbors=3)

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Definir un punto de prueba
X_test = np.array([[4, 3]])

# Realizar la predicción
prediction = clf.predict(X_test)

# Imprimir el resultado
print("El punto", X_test, "se clasifica como:", prediction[0])
