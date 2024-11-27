import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

file = "diabetes.csv"
df = pd.read_csv(file)

data = df.values
X, y = data[:, :-1], data[:, -1]
print(f"Feature shape: {X.shape}, Target shape: {y.shape}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
print(f"Training feature shape: {X_train.shape}, Testing feature shape: {X_test.shape}")
print(f"Training target shape: {y_train.shape}, Testing target shape: {y_test.shape}")

model = KNeighborsClassifier()
model.fit(X_train, y_train)

y_predict = model.predict(X_test)

accuracy = accuracy_score(y_test, y_predict)
print("Dataframe:\n", df.head())
print("Accuracy: {:.2f}%".format(accuracy * 100))

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27],
    [28, 29, 30]
])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

df = pd.DataFrame(X, columns=['Feature1', 'Feature2', 'Feature3'])
df['Target'] = y

X = df.iloc[:, :-1]  # Features
y = df.iloc[:, -1]   # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print("X_train:")
print(X_train)
print("\nX_test:")
print(X_test)
print("\ny_train:")
print(y_train)
print("\ny_test:")
print(y_test)
