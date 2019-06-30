#importing libraries
import pandas as pd
# loading data
df=pd.read_csv('http://13.234.66.67/summer19/datasets/social.csv')
df.info()
df.head()
#removing user ID
filterdata=df.iloc[0:,2:].values
df.head()
# now we can apply training test
features=filterdata[0:,0:2]
#label finding
label=filterdata[0:,2]
from sklearn.model_selection import train_test_split
X,x,Y,y=train_test_split(features,label,test_size=0.2)
# now applying features scalling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
# apply scalling in training data
X=sc.fit_transform(X)
#testing data scalling
x=sc.transform(x)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
#random forest call with number of decision TREE
Rclf=RandomForestClassifier(n_estimators=20)
#now training
trained=Rclf.fit(X,Y)
#prediction
output=trained.predict(x)
print(y)
