# To find the real root of a non-linear equation by bisection method using Python programming
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the equation in x using Python syntax: ")

def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

a, b = float(input("Enter the first initial guess: ")), float(input("Enter the second initial guess: "))

if(f(a)*f(b) > 0):
    print(f"No root lies in the interval ({a}, {b})")
    exit(1)

e, n = float(input("Enter the tolerable error: ")), int(input("Enter the number of iterations: "));

# print(f"\n{"Iteration":<25}{"a":<25}{'b':<25}{"c":<25}{"f(a)":<25}{"f(b)":<25}{"f(c)":<25}")
# print("-"*(7*25))

arr = []
x = np.linspace(-5,5,1000)
midpoints = []

itr = 1
while itr <= n:
    c = (a + b) / 2
    midpoints.append(c)
    arr.append([itr, a, b, c, f(a), f(b), f(c)])
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    err = abs(b - a)
    if(err < e):
        print("\n")
        arr = pd.DataFrame(arr, columns=["Iteration", "a", "b", "c", "f(a)", "f(b)", "f(c)"])
        print(arr.to_string(index=False))
        print(f"\nThe approximate root is {(a+b)/2} with error {err} in {itr} iterations")

        midpoints = np.array(midpoints)

        plt.figure()
        plt.plot(x, f(x), color="r", label=eqn)
        plt.axvline(0, 0, color="black")
        plt.axhline(0, 0, color="black")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.title(f"Solution of {eqn} by bisection method")
        plt.scatter(midpoints, f(midpoints), color="blue")
        for i, val in enumerate(midpoints):
            plt.text(val, f(val), f'{i+1}')
        plt.show()
        break

    # print(f"{itr:<25}{a:<25}{b:<25}{c:<25}{f(a):<25}{f(b):<25}{f(c):<25}")
    itr+=1

if(itr>n):
    print(f"\nSolution does not converge in {n} iterations")