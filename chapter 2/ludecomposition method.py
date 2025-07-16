import numpy as np
import scipy.linalg as la

n = int(input('Enter the order of the square matrix: '))
a = []
for i in range(n):
    a.append(list(map(float, input(f'Enter {i+1}th row: ').split())))
a = np.array(a)
print(f"The matrix A is:\n", np.matrix(a))

b = np.array(list(map(float, input('Enter the constant terms: ').split())))
print(f"The initial vector b is:\n", np.matrix(b))

P, L, U = la.lu(a)
lum = la.lu_factor(a)

print(f"The permutation matrix P is:\n", np.matrix(P))
print(f"The lower triangular matrix L is:\n", np.matrix(L))
print(f"The upper triangular matrix U is:\n", np.matrix(U))

x = la.lu_solve(lum, b)
print(f"The solution vector x is:\n", np.matrix(x))
