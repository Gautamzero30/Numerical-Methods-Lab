# to find te smallest  eigenvalue and eigenvector of a matrix by power method
import numpy as np
import pandas as pd

n = int(input('enter the order of square matrix : '))
a= []
for i in range(n):
    a.append(list(map(float, input(f'enter {i+1}th row : ').split())))
a= np.array(a)    

print(f" the matrix is a \n",np.matrix(a))
def inv(a):
    try:
        return np.linalg.inv(a)
    except:
        print("Matrix is singular and cannot be inverted.")
        return None
b= np.array(inv(a))    
x=np.array(list(map(float, input('enter the initial vector : ').split())))
print(f" the initial vector is x \n",np.matrix(x))
x = np.array(x)
e = float(input('enter the tolerable error : '))
n= int(input('enter the maximum number of iterations : '))
itr = 1
oldev = 0
table =[]
while(itr <= n):
    y = np.dot(b, x)
    maxev = abs(max(y,key = abs))
    for i in range(n):
        x=y/maxev
    err = abs(maxev - oldev)
    if err < e:
        break   
    oldev = maxev
    itr += 1
    table.append({
            "Iteration": itr,
            "maxev": maxev,
            "y": y,
            "x": x
            
        })
if itr > n:
    print(f"\nThe required doesn't converge in {itr} iterations.")  
else:
    print(f"\nThe solution converges in {itr} iterations.")
    print(f"The dominant eigenvalue is : {1/maxev}")
    print(f"The corresponding eigenvector is : \n{np.matrix(x)}")

#the code of the table for the above method is
Table = pd.DataFrame(table)
print(f"the table is ", Table)
      


