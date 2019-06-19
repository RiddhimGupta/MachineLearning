#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
#reading file
sc = pd.read_csv('student.csv') 
#plotting pie-chart
plt.pie(sc['Marks'],labels=sc['Student_Name'],shadow=True,autopct='%1.1f%%',startangle=90)
