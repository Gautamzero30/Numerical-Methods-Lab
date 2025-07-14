import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Allowed math functions for safe eval
allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

def secant_method(f, a, b):
    tol = 1e-6
    iteration = 1
    table = []
    c_values = []

    fa = f(a)
    fb = f(b)

    while abs(b - a) > tol:
        if fb - fa == 0:
            print("Zero division error in formula. Stopping.")
            break

        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        error = abs(c - b)

        print(f"Iteration {iteration}: c = {c}, f(c) = {fc}")

        if fc is None:
            print("Error: f(c) returned None. Stopping.")
            return None

        table.append({
            "Iteration": iteration,
            "a": a,
            "b": b,
            "c": c,
            "f(a)": fa,
            "f(b)": fb,
            "f(c)": fc,
            "Error": error
        })

        c_values.append((c, fc))

        if abs(fc) < tol:
            print("Approximate root found within tolerance!")
            break

        a, fa = b, fb
        b, fb = c, fc
        iteration += 1

    print(f"\nApproximate root after {iteration - 1} iterations: {c}\n")

    df = pd.DataFrame(table)
    print(df.to_string(index=False))

    # ---- Plotting ----
    x_vals = np.linspace(min(a, b) - 1, max(a, b) + 1, 400)
    y_vals = [f(x) for x in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="f(x)", color="blue")
    plt.axhline(0, color="black", linewidth=0.8)

    for i in range(1, len(c_values)):
        x0, y0 = c_values[i - 1]
        x1, y1 = c_values[i]
        plt.plot([x0, x1], [y0, y1], 'k--', alpha=0.5)  # Secant line
        plt.scatter(x1, y1, color="red")
        plt.annotate(f"({x1:.4f}, {y1:.4f})", (x1, y1),
                     textcoords="offset points", xytext=(5, 5), ha='left', fontsize=8)

    plt.axvline(c, color="green", linestyle="--", label=f"Approx Root: {c:.6f}")
    plt.title("Secant Method Graph")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("secant_method_plot.png", dpi=300)
    plt.show()

    return c

# ---- User input ----
user_function = input("Enter a function in terms of x (e.g. cos(x) - x): ")

def f(x):
    try:
        return eval(user_function, {"x": x, **allowed_names}, {})
    except Exception as e:
        print(f"Error evaluating the function at x={x}: {e}")
        return None

a = float(input("Enter the first guess (a): "))
b = float(input("Enter the second guess (b): "))

fa = f(a)
fb = f(b)

if fa is None or fb is None:
    print("Cannot proceed due to errors in function evaluation at the guesses.")
else:
    with open("secant_results.txt", "w") as f_out:
        sys.stdout = f_out
        secant_method(f, a, b)
        sys.stdout = sys.__stdout__

    print("All output saved to secant_results.txt")
