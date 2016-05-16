#!/usr/bin/python

""" 
    (SVM) mini-project.

    SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


### code goes here ###

from sklearn.svm import SVC
clf = SVC(kernel="rbf",C=10000.0)

#slicing the training set to 1% of total data
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

#counting how many test cases are in Chris(1) class
count =0
for a in pred:
    if a==1:
        count = count+1
print "test cases in Chris(1) class: ", count
print "10th element prediction: ", pred[10]
print "26th element prediction: ", pred[26]
print "50th element prediction: ", pred[50]

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print acc
#########################################################


