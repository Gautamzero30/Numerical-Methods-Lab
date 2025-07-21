import numpy as np
import sympy as sp

def divided_diff_table(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:,0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])
    return table

def newton_divided_diff(x, y, value):
    table = divided_diff_table(x, y)
    n = len(x)
    result = table[0,0]
    product = 1.0

    for i in range(1, n):
        product *= (value - x[i-1])
        result += table[0][i] * product

    print("Divided Difference Table:")
    print(table)
    return result

def construct_polynomial(x, y):
    table = divided_diff_table(x, y)
    n = len(x)
    X = sp.Symbol('X')
    polynomial = table[0][0]
    product = 1

    for i in range(1, n):
        product *= (X - x[i-1])
        polynomial += table[0][i] * product

    polynomial = sp.expand(polynomial)
    return polynomial

# Example usage
x = np.array([5, 6, 9, 11])
y = np.array([12, 13, 14, 16])

value = 7

print("\n=== Newton’s Divided Difference Interpolation ===")
interp_value = newton_divided_diff(x, y, value)
print(f"Interpolated value at {value} is {interp_value}")

# Construct and display symbolic polynomial
poly = construct_polynomial(x, y)
print("\nInterpolating Polynomial:")
print(poly)

# Plotting
import matplotlib.pyplot as plt
x_fine = np.linspace(min(x), max(x), 100)
y_fine = [newton_divided_diff(x, y, xi) for xi in x_fine]

plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x_fine, y_fine, label='Newton Divided Difference')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton Divided Difference Interpolation')
plt.legend()
plt.grid(True)
plt.show()
