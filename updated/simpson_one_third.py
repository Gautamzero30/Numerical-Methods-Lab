# to evaluaate integral by simpson's 1/3 rule
import numpy as np
import matplotlib.pyplot as plt

a = float(input("Enter the lower limit: "))
b = float(input("Enter the upper limit: "))

n = int(input("Enter the number of partitions: "))

if n%2 != 0:
    print("Number of partitions must be even")
    exit(1)

h = (b-a)/n

func = input("Enter the integrand function in terms of x using Python syntax: ")

def F(x, func):
    return eval(func)

def y(x):
    return F(x, func)

x = np.linspace(a, b, n+1)


I = 0
S1 = 0
S2 = 0

for i in range(1, n):
    if i%2 != 0:
        S1 +=y(x[i])
    else:
        S2 +=y(x[i])

I = h * (y(x[0]) + 4*S1 + 2*S2 + y(x[n])) / 3

print(f"\nThe approximate integral is {I}")


plt.figure()
plt.plot(x, [y(i) for i in x], label=f"Integration of {func}")
x_val = np.linspace(a-2, b+2, 1000)
plt.plot(x_val, [y(x) for x in x_val])
y_val = [y(x) for x in x]
for i in range(0, n, 2):
    xs = x[i:i+3]
    ys = y_val[i:i+3]
    plt.fill_between(xs, ys, color='pink', edgecolor = 'blue', alpha=0.3)
plt.title("Evaluation of integration by trapezoidal rule.")
plt.legend()
plt.show()