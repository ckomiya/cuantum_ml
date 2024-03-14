import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# gráfico de dispoersión
# Create a scatter plot with a regression line
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 4, 9, 16, 25]
})
sns.regplot(x='x', y='y', data=df)

"""
La función regplot en Seaborn se utiliza para trazar un diagrama 
de dispersión (scatter plot) junto con una línea de regresión lineal 
ajustada a los datos. Esta función es útil para explorar la relación
entre dos variables y visualizar si existe una relación lineal entre ellas. 
"""
plt.show()