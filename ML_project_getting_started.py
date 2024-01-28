# -*- coding: utf-8 -*-
"""ML Project Getting Started.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KjDckwKagO-SyBXeJdP9nAopt--yJp-s
"""

import sys
print('Python: {}'.format(sys.version))
import scipy
print('SciPy: {}'.format(scipy.__version__))
import numpy
print('NumPy: {}'.format(numpy.__version__))
import matplotlib
print('Matplotlib: {}'.format(matplotlib.__version__))
import pandas
print('Pandas: {}'.format(pandas.__version__))
import sklearn
print('Sklearn: {}'.format(sklearn.__version__))

import pandas
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier

#loading data
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

#To understand th dimensions of the dataset
print(dataset.shape)

#To view the data
print(dataset.head(25))

#Statistical summary
print(dataset.describe())

#the class distribution
print(dataset.groupby('class').size())

#Visualising the data using univariate plots
#Box and Whisker Plot
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

#Histogram of the variable
dataset.hist()
pyplot.show()

#Visualising the data using multivariate plots
scatter_matrix(dataset)
pyplot.show()

#Creating validation dataset
#splitting dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.2, random_state=1)

#Building Models

#Logistic Regression
#Linear Discriminant Analysis
#K-Nearest Neighbors
#Classification and Regression Trees
#Gaussian Naive Bayes
#Support Vectoe Machines

models=[]

models.append(('LR',LogisticRegression(solver='liblinear', multi_class='ovr')))

models.append(('LDA',LinearDiscriminantAnalysis()))

models.append(('KNN',KNeighborsClassifier()))

models.append(('NB', GaussianNB()))

models.append(('SVM',SVC(gamma='auto')))

#Evaluating the models
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring ='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

#compare the models
pyplot.boxplot(results,labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

#Predicting on svm
model= SVC(gamma='auto')
model.fit(X_train,Y_train)
predictions = model.predict(X_validation)

# Evaluating the predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

