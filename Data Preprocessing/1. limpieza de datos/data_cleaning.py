import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})

print("Original DataFrame:")
print(df)

# Remove rows with missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)

# Fill missing values with a specific value
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled)

# Fill missing values with mean of the column
df_filled_mean = df.fillna(df.mean())
print("\nDataFrame after filling missing values with mean of the column:")
print(df_filled_mean)