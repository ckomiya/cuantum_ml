from sklearn import svm
import pandas as pd

# Crear un DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'Clase': ['Menor', 'Menor', 'Mayor', 'Mayor', 'Mayor']
})

# Crear un SVM Classifier
clf = svm.SVC(kernel='linear')  # Kernel lineal

# Entrenar el modelo utilizando las características y etiquetas
clf.fit(df[['A']], df['Clase'])

# Predecir la clase para el mismo conjunto de datos (esto es solo para propósitos ilustrativos)
y_pred = clf.predict(df[['A']])
print(y_pred)