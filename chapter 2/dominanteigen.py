# to find te dominant eigenvalue and eigenvector of a matrix
import numpy as np
import pandas as pd

n = int(input('enter the order of square matrix : '))
a= []
for i in range(n):
    a.append(list(map(float, input(f'enter {i+1}th row : ').split())))
a= np.array(a)    
print(f" the matrix is a \n",np.matrix(a))
x=np.array(list(map(float, input('enter the initial vector : ').split())))
print(f" the initial vector is x \n",np.matrix(x))
# x = np.array(x)
e = float(input('enter the tolerable error : '))
n= int(input('enter the maximum number of iterations : '))
itr = 1
oldev = 0
table =[]
while(itr <= n):
    y = np.dot(a, x)
    maxev = abs(max(y))
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
            
        }
        )
    
if itr > n:
    print(f"\nThe required doesn't converge in {itr} iterations.")  
else:
    print(f"\nThe solution converges in {itr} iterations.")
    print(f"The dominant eigenvalue is : {maxev}")
    print(f"The corresponding eigenvector is : \n{np.matrix(x)}")
#the code of the table for the above method is

a = pd.DataFrame(table)
print("the table is \n", a)

      