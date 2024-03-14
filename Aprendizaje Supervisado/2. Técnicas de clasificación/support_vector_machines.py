from sklearn import svm
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [0, 0, 0, 1, 1]
})

# Create a SVM Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel
"""
Cuando se utiliza un kernel lineal (kernel='linear'), el SVC se usa para encontrar el 
hiperplano que mejor separa las diferentes clases en el espacio de características. 
Esto es útil para problemas de clasificación linealmente separables.

'rbf': Para usar un kernel RBF (Función de Base Radial). Este es el kernel predeterminado 
y es útil para problemas donde los datos no son linealmente separables y pueden tener
fronteras de decisión complejas.

'poly': Para un kernel polinomial. Puedes especificar el grado del polinomio con el parámetro degree.

'sigmoid': Para un kernel sigmoide.
"""

# Train the model using the training sets
clf.fit(df[['A']], df['B'])

# Predict the response for test dataset
y_pred = clf.predict(df[['A']])
print(y_pred)