#!/usr/bin/pyhton3
import numpy as np
import random
row=int(input("Enter rows:"))
col=int(input("Enter columns: "))
f=open("array.txt","w")
#Inserting random values in array
x=np.random.randint(9,size=(row,col))
print(x)
f.write('Array\n')
#Saving integer data to array
np.savetxt(f, x,fmt='%d')
