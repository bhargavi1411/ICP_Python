# 3. use the SVM with RBF kernel on the same dataset. How the result changed?

#import packages for support vector , accuracy, split train data and datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets

#load the iris datasets
iris_datasets = datasets.load_iris()

#loading  the iris-datasets samples
x = iris_datasets.data
#getting the samples and feactures of the dataset.
y = iris_datasets.target


#split training and test data for both x and y for linear kernel
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=21)

#split training and test data for both x and y for rbf kernel
train_x1, test_x1, train_y1, test_y1=train_test_split(x, y, test_size=0.2, random_state=21)

#defining the model for linear kernel
lmodel=SVC(kernel='linear')

#defining the model for rbf kernel
rmodel=SVC(kernel='rbf')

#fit training data into linear kernel
lmodel.fit(train_x, train_y)

#predict the test data using linear kernel
prediction=lmodel.predict(test_x)

#calc accuracy score for linear kernel
print("linear kernel Accuracy score is", accuracy_score(prediction, test_y))
#print(prediction)

#fit training data into rbc kernel
rmodel.fit(train_x1, train_y1)

#predict the test data for rbc kernel
pred=rmodel.predict(test_x1)

#calc accuracy for rbc kernel
print("RBF kernel accuracy score is", accuracy_score(pred, test_y1))
#print(pred)