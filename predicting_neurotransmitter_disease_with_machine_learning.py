# -*- coding: utf-8 -*-
"""Predicting Neurotransmitter Disease with Machine Learning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wArY5kWIJJCM9MOsYW-0yk_gHDSE043-
"""

pip install pandas scikit-learn matplotlib seaborn

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Create a simple dataset of neurotransmitter levels
data = {
    'dopamine': [0.5, 0.8, 0.3, 0.6, 0.9, 0.2, 0.4, 0.1, 0.7, 0.85],
    'serotonin': [0.7, 0.5, 0.6, 0.2, 0.1, 0.4, 0.9, 0.8, 0.3, 0.6],
    'gaba': [0.4, 0.3, 0.2, 0.7, 0.6, 0.8, 0.9, 0.5, 0.6, 0.3],
    'disease': [1, 0, 1, 0, 0, 1, 0, 1, 0, 0]  # 1 for disease, 0 for no disease
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)

# Visualize the neurotransmitter data using pairplot
sns.pairplot(df, hue='disease')
plt.show()

# Step 3: Train-Test Split
X = df[['dopamine', 'serotonin', 'gaba']]
y = df['disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train the Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Make Predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy: {:.2f}%".format(accuracy * 100))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 7: Feature Importance Visualization
feature_importance = pd.Series(model.feature_importances_, index=X.columns)
feature_importance.nlargest(3).plot(kind='barh')
plt.title('Feature Importance')
plt.show()

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Create a simple dataset of neurotransmitter levels
data = {
    'dopamine': [0.5, 0.8, 0.3, 0.6, 0.9, 0.2, 0.4, 0.1, 0.7, 0.85],
    'serotonin': [0.7, 0.5, 0.6, 0.2, 0.1, 0.4, 0.9, 0.8, 0.3, 0.6],
    'gaba': [0.4, 0.3, 0.2, 0.7, 0.6, 0.8, 0.9, 0.5, 0.6, 0.3],
    'disease': [1, 0, 1, 0, 0, 1, 0, 1, 0, 0]  # 1 for disease, 0 for no disease
}

print(data)

# Convert to a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)

# Visualize the neurotransmitter data using pairplot
sns.pairplot(df, hue='disease')
plt.show()

# Step 3: Train-Test Split
X = df[['dopamine', 'serotonin', 'gaba']]
Y = df['disease']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Step 4: Train the Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

print(model)

# Step 5: Make Predictions
Y_pred = model.predict(X_test)

print(y_pred)

# Step 6: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy: {:.2f}%".format(accuracy * 100))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 7: Feature Importance Visualization
feature_importance = pd.Series(model.feature_importances_, index=X.columns)
feature_importance.nlargest(3).plot(kind='barh')
plt.title('Feature Importance')
plt.show()