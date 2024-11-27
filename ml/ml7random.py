# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.tree import plot_tree

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Plotting the first decision tree (only one tree)
plt.figure(figsize=(10, 5))
plot_tree(rf_classifier.estimators_[0], filled=True,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          rounded=True, proportion=False)
plt.title("Decision Tree 1")
plt.show()
