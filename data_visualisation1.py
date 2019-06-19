import pandas as pd
import matplotlib.pyplot as plt
sc = pd.read_csv('student.csv')
plt.pie(sc['Marks'],labels=sc['Student_Name'],shadow=True)
