import numpy as np
import math
import matplotlib.pyplot as plt

# Newton Forward Interpolation
def newton_forward(x, y, value):
    n = len(x)
    diff_table = np.zeros((n, n))
    diff_table[:,0] = y

    for i in range(1, n):
        for j in range(n - i):
            diff_table[j][i] = diff_table[j+1][i-1] - diff_table[j][i-1]

    h = x[1] - x[0]
    u = (value - x[0]) / h
    sum = y[0]

    for i in range(1, n):
        u_cal = u_calculate(u, i)
        sum += (u_cal * diff_table[0][i]) / math.factorial(i)

    print("Newton Forward Difference Table:")
    print(diff_table)
    return sum

def u_calculate(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u - i)
    return temp

# Newton Backward Interpolation
def newton_backward(x, y, value):
    n = len(x)
    diff_table = np.zeros((n, n))
    diff_table[:,0] = y

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            diff_table[j][i] = diff_table[j][i-1] - diff_table[j-1][i-1]

    h = x[1] - x[0]
    u = (value - x[-1]) / h
    sum = y[-1]

    for i in range(1, n):
        u_cal = u_calculate_backward(u, i)
        sum += (u_cal * diff_table[n-1][i]) / math.factorial(i)

    print("Newton Backward Difference Table:")
    print(diff_table)
    return sum

def u_calculate_backward(u, n):
    temp = u
    for i in range(1, n):
        temp *= (u + i)
    return temp

# Lagrange Interpolation
def lagrange_interpolation(x, y, value):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (value - x[j]) / (x[i] - x[j])
        result += term
    return result

# Example usage
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 8, 27, 64, 125])  # y = x^3

val = 2.5

print("\n=== Newton Forward Interpolation ===")
print(f"Interpolated value at {val} is {newton_forward(x, y, val)}")

print("\n=== Newton Backward Interpolation ===")
print(f"Interpolated value at {val} is {newton_backward(x, y, val)}")

print("\n=== Lagrange Interpolation ===")
print(f"Interpolated value at {val} is {lagrange_interpolation(x, y, val)}")

# Plotting
plt.scatter(x, y, color='red', label='Data Points')

# Fine-grained X for smooth plotting
x_fine = np.linspace(min(x), max(x), 100)
y_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_fine]
plt.plot(x_fine, y_lagrange, label='Lagrange Interpolation', linestyle='--')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolation Methods')
plt.grid(True)
plt.show()
