import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("Student_Performance.csv")

X = df[['Hours Studied', 'Previous Scores']]
y = df['Performance Index']

print(df.corr())
sns.pairplot(df, x_vars=['Hours Studied', 'Previous Scores'], y_vars='Performance Index', height=4, aspect=1, kind='scatter')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

reg_model = linear_model.LinearRegression()
reg_model.fit(X_train, y_train)

print('Intercept:', reg_model.intercept_)
print('Coefficients:', reg_model.coef_)

y_pred = reg_model.predict(X_test)

mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
r2 = metrics.r2_score(y_test, y_pred)

print('Mean Absolute Error:', mae)
print('Mean Squared Error:', mse)
print('R-squared:', r2)

plt.scatter(y_test, y_pred)
plt.xlabel('Actual Performance Index')
plt.ylabel('Predicted Performance Index')
plt.title('Actual vs Predicted Performance Index')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.show()
