# 1.Implementing Naïve Bayes method using scikit-learn libraryUse iris dataset available
# in https://umkc.box.com/s/pm3cebmhxpnczi6h87k2lwwiwdvtxyk8Use cross validation to create training
# and testing partEvaluate the model on testing part
from sklearn import datasets,metrics
#importing the gussian naive bayes from slearn
from sklearn.naive_bayes import GaussianNB
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split

#loading the  dataset
iris_datasets=datasets.load_iris()


#loading  the iris-datasets samples
x = iris_datasets.data
#getting the samples and feactures of the dataset.
y = iris_datasets.target

#print(irisdatasets.data)

#split the data of arrays or matrices for training and testing cross validation with test size 20%
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=21)

#define the model
model=GaussianNB()

#fit the training data into model
model.fit(x_train,y_train)

#prints the probability of training data
print(f"The Probability of he traning module is {model.score(x_train,y_train)}")

#testing the 20% data which we separated

#define to predict the test data
y_pred = model.predict(x_test)

#calculating the accuracy classification score.
print("The Accuracy score of testing using Naive bayes is : ",metrics.accuracy_score(y_test, y_pred))