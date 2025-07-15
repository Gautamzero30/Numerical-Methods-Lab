# solution of system of equations using guass elimination method by partial pivoting

import numpy as np

n = int(input("Enter the no. of variables: "))
print("Enter augmented matrix: ")
A = []

for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row:: ").split())))
    # row = []
    # for j in range(n+1):
    #     inp = int(input(f"Enter the element A[{i+1}][{j+1}]: "))
    #     row.append(inp)
    # A.append(row)


A = np.array(A)

print("The augmented matrix is:\n", A)

for i in range(n):
    p_row = np.argmax(abs(A[i:, i]))+i
    A[[i, p_row]]= A[[p_row, i]]
    for j in range(i+1, n):
        A[j] = A[j] - A[j, i] * A[i]/A[i, i]


print("The upper triangular matrix is:\n", np.matrix(A))

x = np.zeros(n)

for i in range(n-1, -1, -1):
    for j in range(n):
        if j!=i:
            x[i] = (A[i, -1] - np.sum(A[i, i+1:n] * x[i+1:n]))/A[i, i]

print("The solution is: ")
for i in range(n):
    print(f"x{i+1} = {x[i]}")