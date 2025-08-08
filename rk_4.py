import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ode = input("enter dy/dx in terms of x and y using python syntax: ")

def F(x, y, ode):
    return eval(ode)

def f(x, y):
    return F(x, y, ode)

x = float(input("enter initial value of x: "))
y = float(input("enter initial value of y: "))
h = float(input("enter step size: "))
n = int(input("enter number of steps: "))

l = []
for i in range(n):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x = x + h
    l.append([x, y])

l = pd.DataFrame(l, columns=['x', 'y'])
print(l)

plt.plot(l['x'], l['y'], marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Runge-Kutta Method of Order 4')
plt.grid()
plt.show()
