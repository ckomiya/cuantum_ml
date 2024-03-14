import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Set the plot style to 'whitegrid'
sns.set_style('whitegrid')
#sns.set_style('darkgrid')
#sns.set_style('ticks')

# Create a scatter plot with a regression line
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 4, 9, 16, 25]
})
sns.regplot(x='x', y='y', data=df)
plt.show()