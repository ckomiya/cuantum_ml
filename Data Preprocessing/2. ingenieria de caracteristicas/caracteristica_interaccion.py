import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'height': [5.0, 6.1, 5.6, 5.8, 6.0],
    'width': [3.5, 3.0, 3.2, 3.7, 3.3]
})

# Create a new interaction feature 'area'
df['area'] = df['height'] * df['width']

print(df)