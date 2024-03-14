import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
#print(iris)
"""
Carga el conjunto de datos "iris" de la biblioteca de datos de Seaborn.
Este conjunto de datos contiene mediciones de longitud y ancho del 
sépalo y pétalo de tres especies de iris (setosa, versicolor y virginica).

     sepal_length  sepal_width  petal_length  petal_width    species
0             5.1          3.5           1.4          0.2     setosa
1             4.9          3.0           1.4          0.2     setosa
2             4.7          3.2           1.3          0.2     setosa
3             4.6          3.1           1.5          0.2     setosa
4             5.0          3.6           1.4          0.2     setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica
"""


g = sns.FacetGrid(iris, col="species")

"""
FacetGrid es una clase de Seaborn que se utiliza para crear "grids" de subplots
basados en una o más variables categóricas. En este caso, estamos creando un FacetGrid
basado en el conjunto de datos iris, con una columna para cada especie de iris.   
"""


g.map(plt.hist, "sepal_length")
#g.map(plt.plot, "sepal_length")
"""
map() es un método de FacetGrid que se utiliza para aplicar una función a cada uno 
de los subplots en el grid. En este caso, estamos utilizando plt.hist
(que es una función de Matplotlib para crear histogramas) para trazar un histograma 
de la longitud del sépalo (sepal_length) en cada subplot.  
"""

plt.show()