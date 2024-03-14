from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

# Load the diabetes dataset
diabetes = load_diabetes()
#diabetes = load_iris()

X = diabetes.data
y = diabetes.target

# Create a linear regression model
model = LinearRegression()

# Define the parameter grid
param_grid = {
    'fit_intercept': [True, False],
}
"""
param_grid: Es un diccionario donde las claves son los nombres de los parámetros del modelo
y los valores son listas que contienen los posibles valores que se probarán para cada parámetro.

'fit_intercept': Es el parámetro que indica si el modelo debe ajustar el término de intercepción. 
Se prueba con dos valores booleanos: True y False.

'normalize': Es el parámetro que indica si las características deben normalizarse antes de 
ajustar el modelo. También se prueba con dos valores booleanos: True y False.

Entonces, param_grid define todas las combinaciones posibles de los valores de estos dos
parámetros que se probarán durante la búsqueda de la cuadrícula. Por lo tanto, en total 
se probarán 4 combinaciones:

fit_intercept=True, normalize=True
fit_intercept=True, normalize=False
fit_intercept=False, normalize=True
fit_intercept=False, normalize=False

"""

# Create a GridSearchCV object
grid_search = GridSearchCV(model, param_grid, cv=5)
"""
GridSearchCV realizará una búsqueda exhaustiva de todas estas combinaciones para determinar
cuál proporciona el mejor rendimiento del modelo utilizando la validación cruzada.
"""
# Perform grid search
grid_search.fit(X, y)
"""
grid_search.fit(X, y): Esta línea ejecuta la búsqueda de la cuadrícula utilizando los 
datos de entrada X y las etiquetas y. Durante esta búsqueda, GridSearchCV ajusta el 
modelo con cada combinación de parámetros en el espacio de búsqueda definido por 
param_grid y evalúa el rendimiento del modelo utilizando la estrategia de validación 
cruzada especificada (en este caso, con 5 folds). Esto implica entrenar y evaluar el
modelo varias veces con diferentes combinaciones de parámetros. Una vez completada
la búsqueda, el modelo final se ajusta con los mejores parámetros encontrados.
"""


# Print the best parameters
print(grid_search.best_params_)
"""
print(grid_search.best_params_): Esta línea imprime los mejores parámetros encontrados 
durante la búsqueda de la cuadrícula. Después de que se completa la búsqueda de la 
cuadrícula, el atributo best_params_ de GridSearchCV contiene un diccionario que 
muestra los valores de los parámetros que proporcionaron el mejor rendimiento del
modelo durante la búsqueda. La salida de esta línea mostrará los valores de los 
parámetros que se determinaron como óptimos para el conjunto de datos específico
y el modelo utilizado.


En el contexto de la regresión lineal, el parámetro fit_intercept indica si se debe
ajustar un término de intercepción en el modelo. Cuando fit_intercept está establecido
en True, significa que el modelo de regresión lineal debe estimar tanto los coeficientes
de las características como el término de intercepción. Es decir, el modelo intentará 
encontrar la mejor línea de ajuste que pase por el origen de coordenadas (0,0) y que
también se ajuste a los datos.

Por otro lado, si fit_intercept es False, significa que el modelo no ajustará un término
de intercepción en la línea de regresión y se espera que la línea de regresión pase a 
través del origen de coordenadas (0,0). Esto puede ser adecuado en situaciones donde 
se sabe que la relación entre las características y la variable objetivo pasa por el
origen, como en algunos modelos de ciencia de materiales o física.
"""