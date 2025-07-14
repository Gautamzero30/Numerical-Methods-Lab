import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# ---- Derivative calculator ----
def symbolic_derivative(expr_str):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str, evaluate=False)
    f_prime = sp.diff(expr, x)
    return sp.lambdify(x, f_prime, 'numpy')  # Return numerical function

# ---- Newton-Raphson Method ----
def newton_method(f, df, x0):
    tol = 1e-4
    max_iter = 100
    iteration = 1
    table = []
    x_values = [x0]

    while iteration <= max_iter:
        f_x0 = f(x0)
        df_x0 = df(x0)

        if df_x0 == 0:
            print(f"Zero derivative at iteration {iteration}, x = {x0}. Stopping.")
            break

        x1 = x0 - f_x0 / df_x0
        x_values.append(x1)

        print(f"Iteration {iteration}: x = {x1}, f(x) = {f(x1)}")

        table.append({
            "Iteration": iteration,
            "x": x0,
            "f(x)": f_x0,
            "f'(x)": df_x0,
            "Next x": x1
        })

        if abs(x1 - x0) < tol:
            break

        x0 = x1
        iteration += 1
    else:
        x1 = x0  # Fallback

    df_table = pd.DataFrame(table)
    print("\nIteration Table:")
    print(df_table.to_string(index=False))

    # ---- Plotting ----
    x_vals = np.linspace(x0 - 5, x0 + 5, 400)
    y_vals = [f(x) for x in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(x1, color="green", linestyle="--", label=f"Root ≈ {x1:.4f}")
    plt.scatter(x_values, [f(x) for x in x_values], color="red", label="Iterations", zorder=5)
    plt.title("Newton-Raphson Method")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("newton_method_plot.png", dpi=300, bbox_inches='tight')
    plt.show()

    return x1

# ---- Main Program ----
if __name__ == "__main__":
    # User input
    user_function = input("Enter a function in terms of x (e.g. cos(x) - x): ")
    x0 = float(input("Enter initial guess (x0): "))

    # Define safe evaluation environment
    safe_dict = {
        "x": None,  # Placeholder
        "np": np,
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "exp": np.exp,
        "log": np.log,
        "sqrt": np.sqrt,
        "pi": np.pi,
        "e": np.e,
        "__builtins__": {}
    }

    # Convert string to function
    def f(x):
        safe_dict["x"] = x
        try:
            return eval(user_function, safe_dict)
        except Exception as e:
            print(f"Error evaluating function at x={x}: {e}")
            return None

    # Get derivative function
    df = symbolic_derivative(user_function)
    newton_method(f, df, x0)
