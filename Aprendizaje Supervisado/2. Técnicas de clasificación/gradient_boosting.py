from sklearn.ensemble import GradientBoostingClassifier

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [0, 0, 0, 1, 1]
})


# Create a Gradient Boosting Classifier
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)

"""
n_estimators: Este parámetro especifica el número de estimadores o árboles de decisión que se van a
utilizar en el conjunto de Gradient Boosting. Cada uno de estos estimadores se ajustará secuencialmente
para corregir los errores residuales del modelo anterior. En este caso, se han especificado 
100 estimadores, lo que significa que el algoritmo creará un conjunto de 100 árboles de decisión secuenciales.

learning_rate: El learning rate (tasa de aprendizaje) controla la contribución de cada árbol
al modelo final. Un valor más bajo de learning_rate generalmente requiere un número mayor 
de n_estimators para lograr un buen rendimiento del modelo, pero también puede ayudar a
prevenir el sobreajuste. Aquí, se ha especificado un valor de 1.0, lo que significa que
cada árbol tiene una contribución completa al modelo final.

max_depth: Este parámetro controla la profundidad máxima de cada árbol de decisión en el conjunto.
Una profundidad mayor permite que el modelo capture relaciones más complejas en los datos, pero
también puede llevar al sobreajuste. En este caso, se ha especificado un valor de 1, lo que
significa que cada árbol solo puede tener una profundidad máxima de 1, lo que hace que los 
árboles sean relativamente simples.

random_state: Este parámetro se utiliza para establecer una semilla aleatoria que controla
la aleatorización interna del algoritmo. Fijar este valor garantiza que los resultados sean 
reproducibles y consistentes en diferentes ejecuciones del modelo. En este caso, 
se ha establecido en 0.
"""

# Train the model using the training sets
clf.fit(df[['A']], df['B'])

# Predict the response for test dataset
y_pred = clf.predict(df[['A']])
print(y_pred)