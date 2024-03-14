import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Definir el DataFrame original
data = {
    'X1': [1, 2, 3],
    'X2': [4, 5, 6]
}

df = pd.DataFrame(data)
#print(df)

# Crear un objeto PolynomialFeatures de grado 2
poly = PolynomialFeatures(2)
"""
se crea un objeto de la clase PolynomialFeatures con un parámetro degree igual a 2. 
Este objeto se utilizará para generar características polinomiales de hasta el segundo grado.
La idea detrás de esto es que, si tienes características originales como 'X1' y 'X2', 
el objeto PolynomialFeatures generará automáticamente características adicionales que son
combinaciones polinomiales de las características originales. Por ejemplo, si tienes 'X1' y 'X2',
PolynomialFeatures generará 'X1^2', 'X2^2', 'X1*X2', entre otras.
"""

# Crear características polinomiales
df_poly_array = poly.fit_transform(df)
print(df_poly_array)

# Crear características polinomiales
df_poly_array = poly.fit_transform(df)
"""
Aquí es donde realmente se generan las características polinomiales.
El método fit_transform toma el DataFrame original df como entrada y devuelve un nuevo DataFrame
df_poly_array que contiene las características originales junto con las características 
polinomiales generadas. La palabra "fit" significa que el objeto PolynomialFeatures ajusta 
su comportamiento al DataFrame df proporcionado, es decir, aprende de él para luego transformar
los datos. La palabra "transform" se refiere a la transformación real de los datos, es decir,
generar las características polinomiales según lo aprendido durante el ajuste.
"""

df_poly = pd.DataFrame(df_poly_array, columns=[f"poly_{i}" for i in range(df_poly_array.shape[1])])

print("\nDataFrame con características polinomiales:")
print(df_poly)