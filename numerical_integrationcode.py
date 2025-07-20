import math

# Define your function here
def f(x):
    return x**3 + x**2 + 1

# Midpoint Rule
def midpoint(a, b, n):
    h = (b - a)/n
    result = 0
    for i in range(n):
        xi = a + i*h
        xi_mid = xi + h/2
        result += f(xi_mid)
    return h*result

# Trapezoidal Rule
def trapezoidal(a, b, n):
    h = (b - a)/n
    result = f(a) + f(b)
    for i in range(1, n):
        result += 2 * f(a + i*h)
    return (h/2)*result

# Simpson's 1/3 Rule
def simpson_one_third(a, b, n):
    if n % 2 != 0:
        print("n must be even for Simpson's 1/3 Rule.")
        return None
    h = (b - a)/n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i*h)
        else:
            result += 4 * f(a + i*h)
    return (h/3)*result

# Simpson's 3/8 Rule
def simpson_three_eighth(a, b, n):
    if n % 3 != 0:
        print("n must be multiple of 3 for Simpson's 3/8 Rule.")
        return None
    h = (b - a)/n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * f(a + i*h)
        else:
            result += 3 * f(a + i*h)
    return (3*h/8)*result

# ============================
# Main Program
# ============================

print("Numerical Integration Methods")
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of subintervals n: "))

print("\n--- Results ---")
print(f"Midpoint Rule: {midpoint(a, b, n):.6f}")
print(f"Trapezoidal Rule: {trapezoidal(a, b, n):.6f}")
print(f"Simpson's 1/3 Rule: {simpson_one_third(a, b, n)}")
print(f"Simpson's 3/8 Rule: {simpson_three_eighth(a, b, n)}")
