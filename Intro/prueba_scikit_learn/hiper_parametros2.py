from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create a logistic regression model
model = LogisticRegression(max_iter=1000)  # Ajustamos max_iter para evitar un warning en versiones recientes de scikit-learn

# Define the parameter grid with normalize included
param_grid = {
    'penalty': ['l1', 'l2'],
    'C': [0.1, 1, 10],
    'solver': ['liblinear']
}

# Create a GridSearchCV object
grid_search = GridSearchCV(model, param_grid, cv=5)

# Perform grid search
grid_search.fit(X, y)

# Print the best parameters
print(grid_search.best_params_)
