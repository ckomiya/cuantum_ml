from sklearn.linear_model import LinearRegression
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [3, 4, 5, 6, 7]
})

# Create a LinearRegression model
model = LinearRegression()

# Fit the model
model.fit(df[['A', 'B']], df['C'])

# Predict new values
predictions = model.predict(df[['A', 'B']])

print(predictions)