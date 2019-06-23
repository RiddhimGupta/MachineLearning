from sklearn import datasets
import time
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

#actual data with attributes
features=iris.data

from sklearn.model_selection import train_test_split
label=iris.target

train_data,test_data,label_train,label_test = train_test_split(features,label,test_size=0.1,random_state=0)

#calling decision tree classifier
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
#now time for training clf
trained=clf.fit(train_data,label_train)

#now predicting flowers
predicted_flowers=trained.predict(test_data)

predicted_flowers

label_test

#find accuracy score
from sklearn.metrics import accuracy_score
accuracy_score(label_test,predicted_flowers)
