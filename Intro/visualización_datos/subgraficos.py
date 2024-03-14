import matplotlib.pyplot as plt

# Create a figure and a set of subplots
fig, axs = plt.subplots(2)

"""
plt.subplots(2): Esta función crea una nueva figura y un conjunto de 
subplots (ejes) en esa figura. El argumento 2 especifica que se 
crearán 2 subplots en una columna. Si quieres crear más filas 
o columnas de subplots, simplemente cambia este número.

La función plt.subplots() toma dos argumentos: el número de filas 
y el número de columnas de la cuadrícula de subgráficos. Por ejemplo, 
si deseas crear una cuadrícula de subgráficos de 2x2, llamarías a plt.subplots(2, 2).
"""

# Create a line plot on the first subplot
axs[0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
axs[0].set_title('Square Numbers')

# Create a bar plot on the second subplot
axs[1].bar(['A', 'B', 'C'], [10, 20, 30])
axs[1].set_title('Bar Plot')

# Display the figure and its subplots
plt.tight_layout()

"""
plt.tight_layout() es una función que ajusta automáticamente el espaciado
entre los subplots en una figura para que no haya superposiciones entre
ellos y se utilice de manera más efectiva el espacio disponible en la figura.
Esta función es útil cuando se trabaja con varias subgráficas y
se quiere asegurar que estén bien distribuidas y sean legible

"""
plt.show()
