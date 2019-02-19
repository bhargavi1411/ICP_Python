# 2. Implement linear SVM method using scikit library Use the same dataset above Which algorithm you got better accuracy?
# Can you justify why?

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

#print(y)

#split training and test data for both x and y for linear kernel
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=21)

#define the model with linear kernel
lmodel=SVC(kernel='linear')

#fit training data
lmodel.fit(train_x, train_y)

#predict the test data
prediction=lmodel.predict(test_x)

#calc accuracy score for linear kernel
print("linear kernel Accuracy score is", accuracy_score(prediction, test_y))
#print(prediction)
