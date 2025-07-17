# to  find lagrange interpolation polynomial for the given points
import numpy as np  
import sympy as sp
import matplotlib.pyplot as plt
n = int(input("enter no of points: "))
X = np.array(list(map(float, input("enter x coordinates: ").split())))
Y = np.array(list(map(float, input("enter y coordinates: ").split())))
x= sp.symbols("x")
xp = float(input("enter the point to interpolate :"))

poly = 0
for i in range(n):
    lf = 1
    for j in range(n):
        if j != i:
            lf*=(x-X[j])/(X[i]-X[j])

    poly+= Y[i] *lf
poly = sp.simplify(poly)
print('the lagrange polynomial iis: \n', poly)
int_val=poly.subs(x,xp)
print(f"the interpolated value a x={xp} is {int_val}")
f = sp.lambdify(x,poly,"numpy")
x_val = np.linspace(min(X)-2,max(X)+2,1000)
# graph for the langrange polynomial
plt.figure(figsize=(10, 6))
plt.plot(x_val, f(x_val), label='Lagrange Polynomial', color='blue')
plt.scatter(X, Y, color='red', zorder=5, label='Data Points')
plt.title('Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()