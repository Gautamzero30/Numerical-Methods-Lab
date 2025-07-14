
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# ---- Safe math functions for eval ----
allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

# ---- Choice function ----
def choice(a, b, c, f):
    fa = f(a)
    fc = f(c)
    if fa * fc < 0:
        return a, c
    else:
        return c, b

# ---- False Position Method ----
def false_position(f, a, b):
    tol = 1e-4
    iteration = 1
    table = []
    points_a = []
    points_b = []
    midpoints = []

    while (b - a) / 2 > tol:
        fa = f(a)
        fb = f(b)

        if fb - fa == 0:
            print("Division by zero in False Position formula. Stopping.")
            break

        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        error = (b - a) / 2

        print(f"Iteration {iteration}: c = {c}, f(c) = {fc}")

        if fc is None:
            print("Error: f(c) returned None. Stopping.")
            return None, None

        points_a.append(a)
        points_b.append(b)
        midpoints.append(c)

        table.append({
            "Iteration": iteration,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc,
            "f(a)": fa,
            "f(b)": fb,
            "Error": error,
            "choice": choice(a, b, c, f)
        })

        if abs(fc) < tol:
            print("Function close to zero. Approximate root found.")
            break

        a, b = choice(a, b, c, f)
        iteration += 1

    # Final estimate
    root = (a * f(b) - b * f(a)) / (f(b) - f(a)) if f(b) != f(a) else (a + b) / 2
    print(f"\nApproximate root after {iteration - 1} iterations: {root:.6f}\n")

    df = pd.DataFrame(table)
    print(df.to_string(index=False))

    plot_false_position(f, points_a, points_b, midpoints, root)

    return root, df

# ---- Plotting Function ----
def plot_false_position(f, points_a, points_b, midpoints, root):
    all_points = points_a + points_b + midpoints
    x_min = min(all_points) - 0.5
    x_max = max(all_points) + 0.5

    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = [f(x) for x in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="f(x)", color="blue")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(root, color="green", linestyle="--", label=f"Root ≈ {root:.4f}")

    plt.scatter(all_points, [f(x) for x in all_points], color="red", label="Iterated points", zorder=5)

    plt.title("False Position Method")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("false_position_method.png", dpi=300, bbox_inches='tight')
    plt.show()

# ---- User Input ----
user_function = input("Enter a function in terms of x (e.g. cos(x) - x): ")

def f(x):
    try:
        return eval(user_function, {"x": x, **allowed_names}, {})
    except Exception as e:
        print(f"Error evaluating the function at x={x}: {e}")
        return None

a = float(input("Enter the lower bound (a): "))
b = float(input("Enter the upper bound (b): "))

fa = f(a)
fb = f(b)

if fa is None or fb is None:
    print("Cannot proceed due to errors in function evaluation at interval endpoints.")
elif fa * fb >= 0:
    print("Invalid interval: f(a) and f(b) must have opposite signs.")

false_position(f, a, b)
        