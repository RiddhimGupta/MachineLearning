#Data Engineering
import pandas as pd
#reading csv file from url
df=pd.read_csv('http://13.234.66.67/summer19/datasets/info.csv')

df.info()

df

#removing missing value or replacing with some relevant data
df.describe()

from sklearn.preprocessing import Imputer

imp=Imputer(missing_values='NaN',axis=0,strategy='mean')

#avoids header stores in a variable
X=df.iloc[0:,0:].values

print(X)

#operating column first and second
impute=imp.fit(X[:,1:3])

#time for transforming the fitted columns
X[:,1:3]=impute.transform(X[:,1:3])

#string label int/float
from sklearn.preprocessing import LabelEncoder
cont=LabelEncoder() #this is for country labelling
# now apply column first in this label
X[:,0]=cont.fit_transform(X[:,0])

print(X)

#labeling last column
p=LabelEncoder()
X[:,3]=p.fit_transform(X[:,3])

print(X)

#now encoding first column----making subcolummn of first column
from sklearn.preprocessing import OneHotEncoder
firstcl=OneHotEncoder(categorical_features=[0])
X=firstcl.fit_transform(X).toarray()
X.astype(int)
