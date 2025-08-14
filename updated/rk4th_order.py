# To solve initial value problem of 1st order by using R-K-4 method.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ode = input("Enter dy/dx in terms of x and y using Python sytax: ")

def f(x, y):
    return eval(ode)

x = float(input("Enter the initial value of x: "))
y = float(input("Enter the initial value of y: "))

h = float(input("Enter the step size: "))
n = int(input("Enter the no. of steps: "))

list = []
x_list = []
y_list = []

for i in range(n):
    k1 = h*f(x, y)
    k2 = h*f(x+h/2, y+k1/2)
    k3 = h*f(x+h/2, y+k2/2)
    k4 = h*f(x+h, y+k3)

    y += (k1 + k2 + k3 + k4)/6
    x += h
    list.append([x, y])
    x_list.append(x)
    y_list.append(y)

df = pd.DataFrame(list, columns=['x', 'y'])

print("Solutions:")
print(df)

plt.figure()
plt.plot(x_list, y_list, label="Solution Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Solution of First Order Initial Value Problem by Runge Kutta Method")
plt.show()