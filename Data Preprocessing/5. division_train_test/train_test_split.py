from sklearn.model_selection import train_test_split
import pandas as pd



# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

# Create a target variable
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Perform a train-test split
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)


"""
Lo que hace train_test_split es tomar un conjunto de datos existente, representado por 
el DataFrame df y la variable objetivo y, y dividirlo en dos subconjuntos: uno para 
entrenamiento y otro para pruebas. Este proceso se realiza de forma aleatoria y estratificada,
lo que significa que se preserva la proporción de las clases en la variable objetivo 
en ambos conjuntos. La intención principal de esta división es evaluar el rendimiento 
de un modelo de aprendizaje automático en datos no vistos, es decir, en datos que el
modelo no ha utilizado durante el entrenamiento.

test_size=0.2 especifica que el 20% de los datos se utilizarán como conjunto de prueba, mientras 
que el 80% restante se utilizará como conjunto de entrenamiento.

random_state=42 establece una semilla aleatoria para garantizar que la división de los datos sea reproducible.
Es decir, si ejecutas el código múltiples veces con el mismo valor de random_state, obtendrás la misma
división de datos en conjuntos de entrenamiento y prueba.

Es decir, si se utiliza la misma semilla en diferentes ejecuciones del código, se obtendrá la misma
división de los datos. Esto es útil para fines de reproducibilidad y comparación entre diferentes modelos.

En resumen, al especificar random_state, aseguramos que obtendremos la misma división de los datos
cada vez que ejecutemos el código, lo que facilita la reproducibilidad de los resultados y la 
comparación entre diferentes modelos.

La elección del número específico, como 42, no tiene un significado intrínseco en sí mismo. 
Puede ser cualquier número entero no negativo. Sin embargo, se usa comúnmente números como 42 o 0 
por convención, ya que son fáciles de recordar y tienen una connotación neutral.
"""

print("X_train:")
print(X_train)
print("\nX_test:")
print(X_test)
print("\ny_train:")
print(y_train)
print("\ny_test:")
print(y_test)

""""
Se imprime el conjunto de entrenamiento X_train, que contiene el 80% de las filas de df seleccionadas 
aleatoriamente junto con sus correspondientes etiquetas de clase y_train.

Luego se imprime 
el conjunto de prueba X_test, que contiene el 20% restante de las filas de df junto con sus
etiquetas de clase y_test.
"""