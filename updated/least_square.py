import numpy as np
import matplotlib.pyplot as plt

x = np.array(list(map(float, input("Enter the x-data: ").split())))
y = np.array(list(map(float, input("Enter the y-data: ").split())))

n = len(x)

A = [[n, np.sum(x), np.sum(x*x)], [np.sum(x), np.sum(x*x), np.sum(x**3)], [np.sum(x*x), np.sum(x**3), np.sum(x**4)]]
B = [[np.sum(y)], [np.sum(x*y)], [np.sum((x**2)*y)]]

print("The coefficient matrix of normal eqn:\n", np.matrix(A))
print("The constant matrix of normal eqn:\n", np.matrix(B))

inv_A = np.linalg.inv(A)
coeff = np.dot(inv_A, B)

a = coeff[0]
b = coeff[1]
c = coeff[2]

eqn = f'{a} + {b}x + {c}x^2'
print(f"The curve of best fit is y={eqn}")

def fun(x):
    return a + b*x + c * (x**2)

X = np.linspace(min(x)-2, max(x)+2, 1000)

plt.figure()
plt.plot(X, fun(X), color="r", label=eqn)
plt.axvline(0, 0, color="black")
plt.axhline(0, 0, color="black")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.title(f"Least Square Interpolation")
plt.scatter(x, fun(x), color="red", label="Data Points")

plt.show()