# to calculate the system of lienar eqn by Gauss-Siedal iteration

import numpy as np
import pandas as pd

n = int(input("Enter the no. of variables: "))
print("Enter augmented matrix: ")
A = []
table = []

for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row:: ").split())))

x = np.array(list(map(float, input("Enter initial vector").split())))
A = np.array(A)

print("The initial guess is:\n", np.matrix(x))

e, N = float(input("Enter the tolerable error")), int(input("Enter the max no. of iterations)"))
itr = 1

while(itr <= N):
    x_old = np.copy(x)
    for i in range(n):
        s = 0
        for j in range(n):
            if j!=i:
                s+=A[i, j] * x[j]
        x[i] = (A[i, -1] - s)/A[i,i]
    err = np.abs(x_old-x)
    table.append([itr] + [x[i] for i in range(n)])
    if np.all(err<e):
        break;

    itr += 1
if(itr > N):
    print(f"\nThe required doesn't converge in {itr} iterations.")
else:
    print(f"\nThe solution converges in {itr} iterations.\n")
    table = pd.DataFrame(table, columns= [['Iteration'] + [f"x{i+1}" for i in range(n)]])
    print(table.to_string(index=False))