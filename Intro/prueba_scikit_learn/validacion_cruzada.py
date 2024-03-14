"""

La validación cruzada con cross_val_score en scikit-learn es una técnica comúnmente 
utilizada para evaluar el rendimiento de un modelo de aprendizaje automático. Esta
función realiza la validación cruzada K-fold, que divide el conjunto de datos en K
pliegues (o "folds") de tamaño aproximadamente igual.

Este enfoque proporciona una evaluación más robusta del rendimiento del modelo, ya que 
utiliza todo el conjunto de datos tanto para entrenamiento como para validación,
y cada muestra se utiliza exactamente una vez en el conjunto de validación. 
Esto ayuda a reducir el sesgo de estimación y proporciona una mejor estimación del
rendimiento del modelo en datos no vistos.
"""


from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

# Cargar el conjunto de datos de iris
iris = load_iris()
X = iris.data
y = iris.target

# Crear un clasificador de SVM
clf = SVC(kernel='linear', C=1)
"""
se utiliza la clase SVC (Support Vector Classifier) de scikit-learn para crear un clasificador SVM.

SVM, o Máquinas de Vectores de Soporte (Support Vector Machines), es un algoritmo de aprendizaje 
supervisado que se utiliza tanto para clasificación como para regresión. La idea central
detrás de SVM es encontrar el hiperplano que mejor separa los puntos de datos en diferentes 
clases en un espacio de características de alta dimensión.
"""

# Realizar validación cruzada con 5 folds
scores = cross_val_score(clf, X, y, cv=5)
"""
clf se refiere al modelo de clasificación que hemos creado previamente. En este caso, clf 
es un clasificador SVM con kernel lineal y parámetro de regularización C igual a 1.

Por otro lado, cv=5 es el parámetro que se utiliza para especificar la estrategia de
validación cruzada que se utilizará. En este caso, cv=5 significa que se utilizará
una validación cruzada con 5 folds.

En la validación cruzada con 5 folds, el conjunto de datos se divide en 5 partes iguales.
El modelo se entrena en 4 partes y se evalúa en la parte restante. Este proceso 
se repite 5 veces, de modo que cada parte del conjunto de datos se utiliza una 
vez como conjunto de validación. Luego, los puntajes de rendimiento (por ejemplo,
la precisión en el caso de clasificación) se promedian para obtener una medida 
general del rendimiento del modelo.
"""

# Imprimir los puntajes de la validación cruzada
print("Puntajes de la validación cruzada:", scores)

# Calcular el promedio de los puntajes
print("Promedio de los puntajes:", scores.mean())
