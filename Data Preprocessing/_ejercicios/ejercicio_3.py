# Handling Categorical Data
"""
Dado el siguiente DataFrame, realice una codificación one-hot en la función 'color':
"""
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


# Create a DataFrame
df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red', 'blue']
})

encoder = OneHotEncoder()

# Perform One-Hot Encoding
onehot_encoded_color = encoder.fit_transform(df)

print(onehot_encoded_color)