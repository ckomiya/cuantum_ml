from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [0, 0, 0, 1, 1]
})
# Create a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100)
"""
RandomForestClassifier: Es la clase que implementa el algoritmo de Random Forest 
para problemas declasificación en scikit-learn. Un Random Forest es un conjunto
de árboles de decisión, donde cada árbol se entrena en una submuestra aleatoria 
del conjunto de datos, y la predicción final se obtiene promediando (en clasificación) 
o tomando el voto mayoritario (en clasificación) de los árboles individuales.

n_estimators especifica el número de árboles en el bosque. En este caso, 
se están creando 100 árboles en el bosque. Un mayor número de árboles generalmente 
puede mejorar el rendimiento del modelo, pero también aumenta el tiempo de
entrenamiento y la complejidad del modelo.
"""

# Train the model using the training sets
clf.fit(df[['A']], df['B'])

# Predict the response for test dataset
y_pred = clf.predict(df[['A']])

print(y_pred)