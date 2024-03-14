from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [0, 0, 0, 1, 1]
})

# Create a DecisionTreeClassifier model
model = DecisionTreeClassifier()

# Fit the model
model.fit(df[['A']], df['B'])

# True labels
y_true = df['B']

# Predicted labels
y_pred = model.predict(df[['A']])

# Calculate metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
roc_auc = roc_auc_score(y_true, y_pred)

print("Accuracy:", accuracy)
""" 
Accuracy (Exactitud):
Mide la proporción de predicciones correctas sobre el total de predicciones realizadas.
Se calcula como (Verdaderos positivos + Verdaderos negativos) / (Total de predicciones).
Es una medida general de la precisión del modelo.
"""

print("Precision:", precision)
""" 
Precision (Precisión):
Mide la proporción de instancias clasificadas como positivas que son verdaderamente positivas.
Se calcula como Verdaderos positivos / (Verdaderos positivos + Falsos positivos).
Es útil cuando se quiere evitar clasificar falsos positivos.
"""

print("Recall:", recall)
""" 
Recall (Recuperación o Sensibilidad):
Mide la proporción de instancias verdaderamente positivas que fueron clasificadas correctamente como positivas.
Se calcula como Verdaderos positivos / (Verdaderos positivos + Falsos negativos).
Es útil cuando se quiere evitar clasificar falsos negativos.
"""

print("F1 Score:", f1)
""" 
F1 Score:
Es una medida que combina la precisión y la recuperación en un solo valor.
Se calcula como 2 * (Precision * Recall) / (Precision + Recall).
Es útil cuando se desea una métrica que balancee tanto la precisión como la recuperación.
"""

print("ROC AUC Score:", roc_auc)
""" 
ROC AUC Score:
Es el área bajo la curva ROC (Receiver Operating Characteristic).
La curva ROC representa la tasa de verdaderos positivos frente a la tasa de falsos positivos para 
diferentes umbrales de clasificación.
Cuanto mayor sea el área bajo la curva ROC, mejor será el rendimiento del modelo en general.
"""
