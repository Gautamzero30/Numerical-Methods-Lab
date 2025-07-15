#solution of system of equatinos by gauss jordan method

import numpy as np

n = int(input("Enter the no. of variables: "))
print("Enter augmented matrix: ")
A = []

for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row:: ").split())))


A = np.array(A)

print("The augmented matrix is:\n", A)

for i in range(n):
    p_row = np.argmax(abs(A[i:, i])) + i
    A[[i, p_row]] = A[[p_row, i]]
    A[i] = A[i] / A[i,i]
    for j in range(n):
        if j!=i:
            A[j] = A[j] - A[j, i] * A[i]

print(f"The upper triangular matrix is:\n", np.matrix(A))

x = A[:, -1]

print("The solution is:", x)