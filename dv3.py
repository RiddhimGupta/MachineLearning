# import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('http://13.234.66.67/summer19/datasets/bank.csv')

# create histogram for numeric data
df.hist(figsize=(15,20))
plt.show()

# create bar graph for numeric data 
plt.figure(figsize=(25,20))
plt.bar(df['Age'], df['CreditScore'])
plt.xlabel("Age")
plt.ylabel("CreditScore")
plt.show()

# create pie chart for numeric data
plt.figure(figsize=(15,20))
plt.pie(df['Age'], labels = df['Surname'], autopct ='% 1.1f %%', shadow = True)
plt.show()

# create scatter plot for numeric data
plt.figure(figsize=(30,20))
plt.scatter(df['Balance'], df['Age'])
plt.show()
