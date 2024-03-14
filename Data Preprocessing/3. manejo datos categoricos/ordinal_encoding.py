from sklearn.preprocessing import OrdinalEncoder

# Create a list of categories
categories = [['cold'], ['warm'], ['hot'], ['cold'], ['hot'], ['warm'], ['warm'], ['hot']]

# Create an OrdinalEncoder
encoder = OrdinalEncoder(categories=[['cold', 'warm', 'hot']])

# Perform Ordinal Encoding
ordinal_encoded_categories = encoder.fit_transform(categories)

print(ordinal_encoded_categories)