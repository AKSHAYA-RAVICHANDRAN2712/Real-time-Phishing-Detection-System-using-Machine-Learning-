# Training script for Phishing Detection Model
# This script extracts and runs the key training code from the notebook

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
import pickle
import os

print("Loading dataset...")
# Load the phishing dataset
data = pd.read_csv('phishing.csv')
print(f"Dataset loaded with {len(data)} samples")

# Remove index column if it exists
if 'Index' in data.columns:
    data = data.drop(['Index'], axis=1)

# Split features and target
X = data.drop(["class"], axis=1)
y = data["class"]

print("Splitting data...")
# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Gradient Boosting Classifier...")
# Train the model (using the best performing model from notebook)
gbc = GradientBoostingClassifier(max_depth=4, learning_rate=0.7)
gbc.fit(X_train, y_train)

print("Evaluating model...")
# Make predictions
y_train_pred = gbc.predict(X_train)
y_test_pred = gbc.predict(X_test)

# Calculate accuracy
train_accuracy = metrics.accuracy_score(y_train, y_train_pred)
test_accuracy = metrics.accuracy_score(y_test, y_test_pred)

print(f"Training Accuracy: {train_accuracy:.3f}")
print(f"Test Accuracy: {test_accuracy:.3f}")

# Create pickle directory if it doesn't exist
os.makedirs('pickle', exist_ok=True)

print("Saving model to pickle/model.pkl...")
# Save the model
pickle.dump(gbc, open('pickle/model.pkl', 'wb'))

print("✅ Model training completed successfully!")
print("✅ Model saved as pickle/model.pkl")
print("\nYou can now run your Flask app with: python app.py")