import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'age': [5, 15, 25, 35, 45, 55]
})

# Define bins
bins = [0, 18, 35, 60, 100]

# Define labels
labels = ['child', 'young adult', 'adult', 'senior']

# Perform binning
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

print(df)