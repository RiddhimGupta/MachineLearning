from sklearn import datasets #importing libraries
import time
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

#showing datasets
for i in dir(datasets):
    print(i)
    time.sleep(2)

#this dataset is offline provided by scikit learn
[i for i in dir(datasets) if "load" in i]

#now loading iris data only
iris=load_iris()

#exploring variable
dir(iris)

iris.DESCR

#feature names only
iris.feature_names

#labels or answer
iris.target_names

#actual data with attributes
features=iris.data
features.shape
type(features)
iris.target

sl=features[0:,0]
sw=features[0:,1]
plt.xlabel('length')
plt.ylabel('width')
plt.scatter(sl,sw,label='sepal_data')
plt.scatter(features[0:,2],features[0:,3], label='petal_data',marker='x')
plt.legend()
