from sklearn.linear_model import LogisticRegression
#from sklearn.linear_model import LinearRegression
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [0, 0, 0, 1, 1]
})

# Create a LogisticRegression model
model = LogisticRegression()

# Fit the model
model.fit(df[['A']], df['B'])

# Predict new values
predictions = model.predict(df[['A']])

print(predictions)