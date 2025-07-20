import math

# Define your function here
def f(x):
    return math.sin(x) + x**2

# Forward Difference
def forward_diff(x, h):
    df = (f(x + h) - f(x)) / h
    d2f = (f(x + 2*h) - 2*f(x + h) + f(x)) / (h**2)
    return df, d2f

# Backward Difference
def backward_diff(x, h):
    df = (f(x) - f(x - h)) / h
    d2f = (f(x) - 2*f(x - h) + f(x - 2*h)) / (h**2)
    return df, d2f

# Central Difference
def central_diff(x, h):
    df = (f(x + h) - f(x - h)) / (2*h)
    d2f = (f(x + h) - 2*f(x) + f(x - h)) / (h**2)
    return df, d2f

# ============================
# Main Program
# ============================

print("Numerical Differentiation Methods")
x = float(input("Enter the point x at which to differentiate: "))
h = float(input("Enter step size h: "))

fwd_df, fwd_d2f = forward_diff(x, h)
bwd_df, bwd_d2f = backward_diff(x, h)
cen_df, cen_d2f = central_diff(x, h)

print("\n--- Results ---")
print(f"Forward Difference: f'({x}) = {fwd_df:.6f}, f''({x}) = {fwd_d2f:.6f}")
print(f"Backward Difference: f'({x}) = {bwd_df:.6f}, f''({x}) = {bwd_d2f:.6f}")
print(f"Central Difference: f'({x}) = {cen_df:.6f}, f''({x}) = {cen_d2f:.6f}")
