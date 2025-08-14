# to find the lagarange interpolation polynomial for the given data

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

n = int(input("Enter the no. of data: "))

X = np.array(list(map(float, input("Enter all x-data: ").split())))
y = np.array(list(map(float, input("Enter all y-data: ").split())))

xp = float(input("Enter point to interpolate: "))

x = sp.symbols('x')

poly = 0

for i in range(n):
    lf = 1
    for j in range(n):
        if(j!=i):
            lf *= (x - X[j])/(X[i]-X[j])    
    poly += lf * y[i]

poly = sp.simplify(poly)

print("The Lagarange polynomial is:\n", poly)

int_val = poly.subs(x, xp)
print(f"The interpolated value at x = {xp} is {int_val}")

f = sp.lambdify(x, poly, "numpy")
x_val = np.linspace(min(X)-2, max(X)+2, 1000)

#visualize the output
plt.figure()
plt.plot(x_val, f(x_val), color="r", label=poly)
plt.axvline(0, 0, color="black")
plt.axhline(0, 0, color="black")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.title(f"Lagarange Interpolation")
plt.scatter(X, f(X), color="blue")
for i, val in enumerate(X):
    plt.text(val, f(val), f'{val}')
plt.scatter(xp, f(xp), color="red")
plt.text(xp, f(xp), f'{xp}')
plt.show()