from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

# Cargar el conjunto de datos de diabetes de ejemplo
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

"""
data: Este atributo contiene los datos de entrada o características del conjunto de datos. 
Cada fila representa un paciente, y cada columna representa una característica relevante, 
como la edad, el sexo, el índice de masa corporal, la presión arterial, etc. Cada valor 
en la matriz representa una medición específica para un paciente en una característica particular.

target: Este atributo contiene los valores objetivo o etiquetas asociadas con los datos de entrada.
En este caso, los valores objetivo son medidas cuantitativas de la progresión de la enfermedad 
un año después del inicio del estudio en pacientes con diabetes.
"""

# Crear un modelo de regresión lineal
model = LinearRegression()

# Realizar validación cruzada con 5 folds
scores = cross_val_score(model, X, y, cv=5)

# Imprimir los puntajes de la validación cruzada
print("Puntajes de la validación cruzada:", scores)

# Calcular el promedio de los puntajes
print("Promedio de los puntajes:", scores.mean())


"""
En el contexto del ejemplo de load_diabetes() utilizando cross_val_score con 5 folds y 
obteniendo un promedio de puntajes de 0.48, puede interpretarse como un rendimiento moderado
del modelo de regresión lineal en el conjunto de datos de diabetes.

El puntaje obtenido (0.48) representa la medida de rendimiento del modelo, que en este caso
puede ser el coeficiente de determinación R². Este valor indica cuánta variabilidad en la
variable de respuesta (en este caso, la progresión de la enfermedad de la diabetes) 
puede explicar el modelo. Un valor de R² cercano a 1 indica un buen ajuste del modelo a los datos, 
mientras que un valor cercano a 0 indica que el modelo no puede explicar bien la variabilidad 
en la variable de respuesta.

Un puntaje de 0.48 podría considerarse moderado. Indica que aproximadamente el 48% de la 
variabilidad en la progresión de la enfermedad de la diabetes puede explicarse por las 
características (datos de entrada) utilizadas en el modelo de regresión lineal. Aunque 
no es un puntaje muy alto, tampoco es extremadamente bajo. Sugiere que el modelo tiene
cierta capacidad para predecir la progresión de la enfermedad de la diabetes, pero puede
haber margen para mejorar el rendimiento del modelo mediante ajustes adicionales o la
inclusión de características más relevantes.

"""
