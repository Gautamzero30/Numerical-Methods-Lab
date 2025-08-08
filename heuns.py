import pandas as pd
import matplotlib.pyplot as plt

ode = input("Enter dy/dx in terms of x and y using Python syntax: ")

def F(x, y, ode):
    return eval(ode)

def f(x, y):
    return F(x, y, ode)

x = float(input("Enter initial value of x: "))
y = float(input("Enter initial value of y: "))
h = float(input("Enter step size: "))
n = int(input("Enter number of steps: "))

results = [[x, y]]

for i in range(n):
    y_predictor = y + h * f(x, y)
    y_corrector = y + (h / 2) * (f(x, y) + f(x + h, y_predictor))
    x += h
    y = y_corrector
    results.append([x, y])

df = pd.DataFrame(results, columns=['x', 'y'])
print("\nIteration Table:")
print(df)

plt.plot(df['x'], df['y'], marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Heun's Method (Improved Euler)")
plt.grid()
plt.show()
