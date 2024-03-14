import pandas as pd


df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
})

# Calculate the mean of a column
print(df['A'].mean())

# Calculate the sum of a column
print(df['A'].sum())

# Calculate the maximum value of a column
print(df['A'].max())

# Calculatethe minimum value of a column
print(df['A'].min())


print("\n estadísticas resumidas para la columna A")
print(df['A'].describe())