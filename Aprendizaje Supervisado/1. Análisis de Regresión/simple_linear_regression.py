from sklearn.linear_model import LinearRegression
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5], # caracteristicas o variables independientes
    'B': [2, 4, 5, 4, 5]  # variable dependiente o valores reales u
})

# Create a LinearRegression model
model = LinearRegression()

# Fit the model
model.fit(df[['A']], df['B'])

# Predict new values
predictions = model.predict(df[['A']])
print(predictions)


new_predict = pd.DataFrame({'A': [8]})
print(new_predict)
