# Newton Rhapson
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the equation in python syntax: ")

def F(x, eqn):
    return eval(eqn);

def f(x):
    return F(x, eqn)

def g(f, x, h=1e-10):
    return ((f(x+h) - f(x-h)) / (2*h))

a = float(input("Enter the initial guess:"))
if g(f, a) == 0:
    print(f"The function is not differentiable at x={a}, try different initial guess!\n")
    exit(-1)

e, N = float(input("Enter tolerable error: ")), int(input("Enter the max no. of iterations: "))
table = []
scatter_points = []
x = np.linspace(-20, 20, 5000)
itr = 1

while itr <= N:
    b = a - f(a)/g(f, a)
    err = abs(f(b))

    table.append({
        "Iterations": itr,
        "a": a,
        "b": b,
        "f(a)": f(a),
        "f(b)": f(b),

    })

    scatter_points.append(b)

    if err < e:
        break;

    a = b
    if(g(f, a) == 0):
        print("\nThe function isn't differentiable at {a}, try different initial guess");
        exit(-1)
    
    itr += 1

if(itr > N):
    print(f"\nSolution does not converge in {itr} iterations.")
else:
    print(f"\nRoot found at {b} in {itr} iterations\n")
    table = pd.DataFrame(table)
    scatter_points = np.array(scatter_points)
    print(table.to_string(index=False))
    plt.figure()
    plt.plot(x, f(x), label=eqn, color="r")
    plt.scatter(scatter_points, f(scatter_points), color="b")
    plt.axvline(0, 0, color="black")
    plt.axhline(0, 0, color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.title(eqn)
    for i, val in enumerate(scatter_points):
        plt.text(val, f(val), f'{i+1}')
    plt.show()
