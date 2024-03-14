from scipy import stats
import numpy as np

# Create a numpy array with outliers
data = np.array([1, 2, 2, 2, 3, 1, 2, 3, 3, 4, 4, 4, 20])
print(type(data))

# Calculate Z-scores
z_scores = stats.zscore(data)
"""
Los Z-scores son una medida de cuántas desviaciones estándar un punto de datos está lejos de la media.
Esto permite identificar valores atípicos que se desvían significativamente de la distribución de los datos.
"""
print(f"z_scores: {z_scores}")

# Get indices of outliers
outliers = np.abs(z_scores) > 2
"""
Se definen los outliers como aquellos puntos de datos cuyos Z-scores absolutos son mayores que 2. 
Esto significa que si el valor absoluto del Z-score de un punto de datos es mayor que 2, 
se considera un valor atípico.
"""
print(f"index outliers: {outliers}")

# Remove outliers
data_clean = data[~outliers]
"""
Se utiliza una máscara booleana para seleccionar los valores que no son outliers.
Con la expresión data[~outliers], se eliminan los outliers del array data utilizando
la operación de indexación booleana.
"""

print("Data after removing outliers:")
print(data_clean)