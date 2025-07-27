import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the second-order ODE right-hand side function: y'' = f(x)
def f(x):
    return -pi**2 * np.sin(pi * x)

# Finite Difference Method Implementation
def finite_difference_method(a, b, alpha, beta, f, n):
    """
    Solves y'' = f(x) on [a, b] with y(a)=alpha and y(b)=beta using Finite Difference Method.
    n: number of internal points (not including boundaries)
    """
    h = (b - a) / (n + 1)
    x = np.linspace(a + h, b - h, n)
    rhs = np.array([f(xi) for xi in x])

    # Tridiagonal matrix A
    A = np.zeros((n, n))
    for i in range(n):
        A[i, i] = -2
        if i > 0:
            A[i, i - 1] = 1
        if i < n - 1:
            A[i, i + 1] = 1

    # Adjust RHS for boundary conditions
    rhs[0] -= alpha
    rhs[-1] -= beta

    # Solve system
    y_internal = np.linalg.solve(A / h**2, rhs)

    # Include boundary points
    x_full = np.concatenate(([a], x, [b]))
    y_full = np.concatenate(([alpha], y_internal, [beta]))

    return x_full, y_full

# === Problem Setup ===
a = 0
b = 1
alpha = 0
beta = 0
n = 10  # number of internal points

# Solve using FDM
x_vals, y_vals = finite_difference_method(a, b, alpha, beta, f, n)

# Exact solution
exact_vals = np.sin(pi * np.array(x_vals))

# === Plotting ===
plt.plot(x_vals, y_vals, 'ro-', label='FDM Solution')
plt.plot(x_vals, exact_vals, 'b--', label='Exact: sin(pi x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Finite Difference Method vs Exact Solution')
plt.grid(True)
plt.legend()
plt.show()

# === Print Results ===
print("\n  x\t\tFDM y(x)\tExact y(x)")
for xi, yi, ei in zip(x_vals, y_vals, exact_vals):
    print(f"{xi:.5f}\t{yi:.6f}\t{ei:.6f}")
