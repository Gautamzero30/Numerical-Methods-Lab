import sympy as sp

# Define variables
x, y = sp.symbols('x y')

# Given function
f = x + y

# Derivatives needed
f1 = f
f2 = sp.diff(f, x) + sp.diff(f, y) * f
f3 = sp.diff(f2, x) + sp.diff(f2, y) * f

# Convert to lambda functions for evaluation
f1_func = sp.lambdify([x, y], f1)
f2_func = sp.lambdify([x, y], f2)
f3_func = sp.lambdify([x, y], f3)

# Initial conditions
x0 = 0
y0 = 1
h = 0.1

# Evaluate derivatives at (x0, y0)
f1_val = f1_func(x0, y0)
f2_val = f2_func(x0, y0)
f3_val = f3_func(x0, y0)

# Taylor series expansion
y1 = y0 + h*f1_val + (h**2/2)*f2_val + (h**3/6)*f3_val

# Display results
print("f(x,y) =", f1_val)
print("f'(x,y) =", f2_val)
print("f''(x,y) =", f3_val)
print("Approximate y(0.1) =", y1)
