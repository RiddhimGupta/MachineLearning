#!/usr/bin/python3
import numpy as np
#arange*(start,stop,step)[values to be included].reshape(rows,columns)
arr=np.arange(100,200,5)[0:16].reshape(8,2)
#printing the newly generated array
print(arr)
