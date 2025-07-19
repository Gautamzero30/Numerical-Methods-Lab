"""
Here is a **complex Numerical Methods code** implementing multiple methods:
1. Bisection Method
2. Newton-Raphson Method
3. Secant Method
4. False Position Method
5. Fixed Point Iteration

All methods are structured within a single Python program with:
- Modular functions
- Iteration tables printed nicely
- Matplotlib plotting
- Final summary comparison

You can use it for your Numerical Methods advanced practice, project preparation, or engineering lab.
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def bisection(a, b, tol=1e-5, max_iter=100):
    print("\n--- Bisection Method ---")
    if f(a)*f(b) >= 0:
        print("Invalid interval.")
        return None
    for i in range(max_iter):
        c = (a + b)/2
        print(f"Iter {i+1}: c={c:.6f}, f(c)={f(c):.6f}")
        if abs(f(c)) < tol:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return c

def newton_raphson(x0, tol=1e-5, max_iter=100):
    print("\n--- Newton-Raphson Method ---")
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)/df(x)
        print(f"Iter {i+1}: x={x_new:.6f}, f(x)={f(x_new):.6f}")
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def secant(x0, x1, tol=1e-5, max_iter=100):
    print("\n--- Secant Method ---")
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Divide by zero error.")
            return None
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        print(f"Iter {i+1}: x={x2:.6f}, f(x)={f(x2):.6f}")
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x2

def false_position(a, b, tol=1e-5, max_iter=100):
    print("\n--- False Position Method ---")
    if f(a)*f(b) >= 0:
        print("Invalid interval.")
        return None
    for i in range(max_iter):
        c = b - f(b)*(b-a)/(f(b)-f(a))
        print(f"Iter {i+1}: c={c:.6f}, f(c)={f(c):.6f}")
        if abs(f(c)) < tol:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return c

def fixed_point(x0, tol=1e-5, max_iter=100):
    print("\n--- Fixed Point Iteration ---")
    g = lambda x: (x + 2/x**2)/2  # Rearranged form for this specific f(x)
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        print(f"Iter {i+1}: x={x_new:.6f}, f(x)={f(x_new):.6f}")
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Running all methods
root_bisect = bisection(1, 2)
root_newton = newton_raphson(1.5)
root_secant = secant(1, 2)
root_false = false_position(1, 2)
root_fixed = fixed_point(1.5)

# Plotting
x = np.linspace(0, 2, 100)
y = f(x)
plt.figure(figsize=(8,6))
plt.plot(x, y, label='f(x) = x^3 - x - 2')
plt.axhline(0, color='black', lw=0.5)
plt.scatter([root_bisect, root_newton, root_secant, root_false, root_fixed],
            [f(root_bisect), f(root_newton), f(root_secant), f(root_false), f(root_fixed)],
            color=['red','blue','green','purple','orange'],
            label='Roots by methods')
plt.legend()
plt.title('Root Finding Methods Comparison')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# Final summary
print("\n=== Root Finding Summary ===")
print(f"Bisection: {root_bisect:.6f}")
print(f"Newton-Raphson: {root_newton:.6f}")
print(f"Secant: {root_secant:.6f}")
print(f"False Position: {root_false:.6f}")
print(f"Fixed Point: {root_fixed:.6f}")

"""
**Next steps for your practice:**
- Modify f(x) to other nonlinear equations.
- Change g(x) in fixed point iteration accordingly.
- Use these codes in your Numerical Methods practical files with explanation.
If you want, I can prepare LaTeX reports or problem sets based on these for your upcoming NM preparation this week.
"""
