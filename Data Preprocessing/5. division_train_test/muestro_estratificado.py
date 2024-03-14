from sklearn.model_selection import train_test_split
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

# Create a target variable with imbalanced class distribution
y = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

# Perform a train-test split with stratified sampling
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42, stratify=y)

print("y_train:")
print(y_train)
print("\ny_test:")
print(y_test)

"""
stratify se utiliza para garantizar que las proporciones de las clases en el conjunto de datos 
se mantengan en los conjuntos de entrenamiento y prueba.

En tu caso, la variable y tiene una distribución desigual de clases, donde el 70% de las instancias
son de la clase 0 y el 30% son de la clase 1. Al especificar stratify=y, el conjunto de entrenamiento
y el conjunto de prueba tendrán la misma proporción de clases que el conjunto original. 
Por lo tanto, aproximadamente el 70% de las instancias en ambos conjuntos (entrenamiento y prueba)
serán de la clase 0, y el 30% restante serán de la clase 1.

Esto es útil para asegurarse de que los conjuntos de entrenamiento y prueba sean representativos
de la distribución original de las clases y evitar un sesgo en la evaluación del modelo, 
especialmente en casos de conjuntos de datos desequilibrados.

"""