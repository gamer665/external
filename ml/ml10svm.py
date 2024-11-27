import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC 
fish=pd.read_csv("Experiment10.csv") 
X=fish.drop(['Species'], axis = 'columns') 
y = fish. Species

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model =SVC(kernel = 'linear', C=1)

model.fit(X_train, y_train) 
svm_pred= model.predict(X_test) 
accuracy= model.score(X_test, y_test) 
print(f"accuracy : {accuracy}") 
print(svm_pred)