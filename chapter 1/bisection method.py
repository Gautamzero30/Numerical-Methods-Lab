import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Allow only safe math functions
allowed_names = {
    **{k: v for k, v in math.__dict__.items() if not k.startswith("__")},
    "ln": math.log,       # alias for natural log
    "log10": math.log10,  # base-10 log
    "e": math.e,
    "pi": math.pi
}

def choice(a, b, c, f):
    fa = f(a)
    fc = f(c)
    if fa * fc < 0:
        return a, c
    else:
        return c, b

def bisection(f, a, b):
    tol = 1e-3
    iteration = 1
    table = []
    c_values = []

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        error = (b - a) / 2
        print(f"Iteration {iteration}: c = {c}, f(c) = {fc}")

        if fc is None:
            print("Error: f(c) returned None. Stopping.")
            return None

        table.append({
            "Iteration": iteration,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc,
            "f(a)": f(a),
            "f(b)": f(b),
            "Error": error,
            "choice": choice(a, b, c, f)
        })

        c_values.append(c)

        if abs(fc) < tol:
            print("Approximate root found!")
            break

        a, b = choice(a, b, c, f)
        iteration += 1

    root = (a + b) / 2
    print(f"\nApproximate root after {iteration - 1} iterations: {root}\n")

    # Print iteration table
    df = pd.DataFrame(table)
    print(df.to_string(index=False))

    # ---- Plotting ----
    x_vals = np.linspace(original_a, original_b, 400)
    y_vals = []
    for x in x_vals:
        try:
            y_vals.append(f(x))
        except:
            y_vals.append(None)

    plt.figure(figsize=(10, 6))
    plt. plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(root, color="green", linestyle="--", label=f"Approx Root: {root:.4f}")
    plt.scatter(c_values, [f(c) for c in c_values], color="red", label="Midpoints (c)", zorder=5)
    plt.title("Bisection Method")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("bisection_method_plot.png", dpi=300, bbox_inches='tight')
    plt.show()

    return root

# ---- User input ----
print("Supported functions: sin, cos, tan, exp, log, log10, ln, sqrt, etc.")
print("Use 'x' as the variable (e.g. exp(x) - 3*x)")
user_function = input("Enter a function in terms of x: ")

def f(x):
    try:
        return eval(user_function, {"x": x, **allowed_names}, {})
    except Exception as e:
        print(f"Error evaluating the function at x={x}: {e}")
        return None

try:
    a = float(input("Enter the lower bound (a): "))
    b = float(input("Enter the upper bound (b): "))
except ValueError:
    print("Invalid numeric input.")
    sys.exit(1)

# Save original interval for plotting
original_a = a
original_b = b

fa = f(a)
fb = f(b)

if fa is None or fb is None:
    print("Cannot proceed due to errors in function evaluation at the interval endpoints.")
elif fa * fb >= 0:
    print("Invalid interval: f(a) and f(b) must have opposite signs.")
else:
    bisection(f, a, b)
