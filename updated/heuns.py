# to solve first order ivp by Heuns method
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
    y_predictor = y + h*f(x, y)
    y_corrector = y + (h / 2) * (f(x, y) + f(x + h, y + y_predictor))
    y = y_corrector
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