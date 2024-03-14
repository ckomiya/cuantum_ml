from sklearn.preprocessing import LabelEncoder

# Create a list of categories
categories = ['red', 'blue', 'green', 'red', 'green', 'blue', 'blue', 'green']

# Create a LabelEncoder
encoder = LabelEncoder()

# Perform Label Encoding
encoded_categories = encoder.fit_transform(categories)

print(encoded_categories)  # imprime: [2 0 1 2 1 0 0 1]