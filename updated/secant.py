# to find a real root of non-linear equatino by secant method using python programming
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the equation in python syntax: ")

def F(x, eqn):
    return eval(eqn);

def f(x):
    return F(x, eqn)

a, b = float(input("Enter two initial guesses: ")), float(input())

if f(a) == f(b):
    print("The value becomes infinite, try other choices.")
    exit(-1)

e, N = float(input("Enter the tolerable error: ")), int(input("Enter the max. no of iterations: "))

table = []
plot_points = []

x = np.linspace(-5, 5, 1000)

itr = 1;

# print(f"\n{"Iteration":<25}{"a":<25}{'b':<25}{"c":<25}{"f(a)":<25}{"f(b)":<25}{"f(c)":<25}")
# print("-"*(7*25))

while itr <= N:
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    err = abs(f(c))

    table.append({
        "Iteration": itr,
        "a": a,
        "b": b,
        "c": c,
        "f(a)": f(a),
        "f(b)": f(b),
        "f(c)": f(c),
        "error": err
    })

    plot_points.append(c)

    if err < e:
        break

    a, b = b, c


    if(f(a) == f(b)):
        print("\nDivision by zero error! Change initial guess\n")
        exit(-1)

    # print(f"{itr:<25}{a:<25}{b:<25}{c:<25}{f(a):<25}{f(b):<25}{f(c):<25}")

    itr+=1

if itr > N:
    print(f"\nNo root found in {itr} iterations.")
else :
    print(f"\nSolution found at {c} in {itr} iterations.\n")
    table = pd.DataFrame(table)
    plot_points = np.array(plot_points)
    print(table.to_string(index=False))
    plt.figure()
    plt.plot(x, f(x), label=eqn, color="r")
    plt.scatter(plot_points, f(plot_points), color="b")
    plt.axvline(0, 0, color="black")
    plt.axhline(0, 0, color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.title(eqn)
    for i, val in enumerate(plot_points):
        plt.text(val, f(val), f'{i+1}')
    plt.show()
