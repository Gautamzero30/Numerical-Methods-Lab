# to evaluate integration of a function by trapezoidal rule
import numpy as np
import matplotlib.pyplot as plt

a = float(input("Enter the lower limit: "))
b = float(input("Enter the upper limit: "))

n = int(input("Enter the number of partitions: "))

h = (b-a)/n

func = input("Enter the integrand function in terms of x using Python syntax: ")

def F(x, func):
    return eval(func)

def y(x):
    return F(x, func)

x = np.linspace(a, b, n+1)


I = 0
S = 0

# S += (y(x[i]) for i in range(1, n))
for i in range(1, n):
    S += y(x[i])

I = h * (y(x[0]) + 2 * S + y(x[n])) / 2

print(f"\nThe approximate integrate value is {I}")


plt.figure()
plt.plot(x, [y(i) for i in x], label=f"Integration of {func}")
x_val = np.linspace(a-10, b+10, 1000)
plt.plot(x_val, [y(x) for x in x_val])
y_val = [y(x) for x in x]
for i in range(n):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, y_val[i], y_val[i+1], 0]
    plt.fill(xs, ys, color='pink', edgecolor = 'blue', alpha=0.3)
plt.title("Evaluation of integration by trapezoidal rule.")
plt.legend()
plt.show()