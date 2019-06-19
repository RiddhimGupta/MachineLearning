import numpy as np
a=int(input("Enter rows:"))
b=int(input("Enter columns: "))
out=''
f=open("array.txt","w")
x=np.full((a,b),6)
print(x)
f.write('Array\n')
c = np.array2string(x)  # '[[1 2]\n [3 4]\n [5 6]]'. You can save this. Or
np.savetxt(f, x,fmt='%d')
