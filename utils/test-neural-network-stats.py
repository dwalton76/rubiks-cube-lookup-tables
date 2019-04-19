#!/usr/bin/env python3

import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn

'''
print('Python: {}'.format(sys.version))
print('scipy: {}'.format(scipy.__version__))
print('numpy: {}'.format(numpy.__version__))
print('matplotlib: {}'.format(matplotlib.__version__))
print('pandas: {}'.format(pandas.__version__))
print('sklearn: {}'.format(sklearn.__version__))
'''

# Load libraries
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection, preprocessing
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# Load dataset
columns = ['centers-one-color', 'centers-horizontal-bars', 'centers-vertical-bars', 'centers-l-pattern', 'centers-single-horizontal-bar', 'centers-single-vertical-bar', 'UD-cost', 'LR-cost', 'FB-cost', 'move-count']
COLUMNS_LEN = len(columns)

with open('lookup-table-4x4x4-step10-ULFRBD-centers-stage.txt.nn', 'r') as fh:
    dataset = pandas.read_csv(fh, names=columns)

print(type(dataset))

# mean removal
print("\nMean BEFORE:")
print(dataset.mean(axis=0))
print("\nStandard Deviation BEFORE:")
print(dataset.std(axis=0))

# StandardScaler: mean=0, variance=1
dataset_scaled = preprocessing.StandardScaler().fit_transform(dataset)
#dataset_scaled = preprocessing.scale(dataset)
print(type(dataset_scaled))

print("\nMean AFTER:")
print(dataset_scaled.mean(axis=0))
print("\nStandard Deviation AFTER:")
print(dataset_scaled.std(axis=0))

print('shape\n=====')
print(dataset.shape)
print('')


print('head\n====')
print(dataset.head(20))
print('')

# descriptions
print('descriptions\n============')
print(dataset.describe())
print('')

print('distribution\n============')
print(dataset.groupby('move-count').size())
print('')


# box and whisker plots
#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
#plt.show()


# histograms
#dataset.hist()
#plt.show()

# scatter plot matrix
#scatter_matrix(dataset)
#plt.show()


# Split-out validation dataset
array = dataset.values
X = array[:,0:COLUMNS_LEN-1]
Y = array[:,COLUMNS_LEN-1]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'



# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
#models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
#models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []

for (name, model) in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
print('')

# Compare Algorithms
#fig = plt.figure()
#fig.suptitle('Algorithm Comparison')
#ax = fig.add_subplot(111)
#plt.boxplot(results)
#ax.set_xticklabels(names)
#plt.show()


# Make predictions on validation dataset
#knn = KNeighborsClassifier()
#knn.fit(X_train, Y_train)
#predictions = knn.predict(X_validation)

cart = DecisionTreeClassifier()
cart.fit(X_train, Y_train)
predictions = cart.predict(X_validation)

print("accuracy score")
print("==============")
print(accuracy_score(Y_validation, predictions))
print('')

print("confusion matrix")
print("================")
print(confusion_matrix(Y_validation, predictions))
print('')

print("classification report")
print("=====================")
print(classification_report(Y_validation, predictions))
print('')
