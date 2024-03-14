
"""
Train-Test Split
----------------
Dado el siguiente marco de datos y la variable de destino, 
realice una división de entrenamiento y prueba con un tamaño de prueba
de 0.3 y un estado aleatorio de 42:
"""

import pandas as pd
from sklearn.model_selection import train_test_split

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

# Create a target variable
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Perform a train-test split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3, random_state=42)

print("X_train:")
print(X_train)
print("\nX_test:")
print(X_test)
print("\ny_train:")
print(y_train)
print("\ny_test:")
print(y_test)
