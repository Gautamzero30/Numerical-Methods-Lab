def f(x, y1, y2):
    """Defines the second-order ODE: y'' = f(x, y, y')"""
    return -y1  # Example: y'' = -y (simple harmonic oscillator)

def rk4_system(f, x0, y10, y20, h, xn):
    """Solves the system of ODEs using RK4"""
    x = x0
    y1 = y10
    y2 = y20

    while x < xn:
        k1 = h * y2
        l1 = h * f(x, y1, y2)

        k2 = h * (y2 + l1 / 2)
        l2 = h * f(x + h / 2, y1 + k1 / 2, y2 + l1 / 2)

        k3 = h * (y2 + l2 / 2)
        l3 = h * f(x + h / 2, y1 + k2 / 2, y2 + l2 / 2)

        k4 = h * (y2 + l3)
        l4 = h * f(x + h, y1 + k3, y2 + l3)

        y1 += (k1 + 2*k2 + 2*k3 + k4) / 6
        y2 += (l1 + 2*l2 + 2*l3 + l4) / 6
        x += h

    return y1  # returns y(b) for current slope guess

def shooting_method(f, a, b, alpha, beta, s1, s2, h, tol=1e-5):
    """Solves the BVP using the shooting method with secant iteration"""
    yb1 = rk4_system(f, a, alpha, s1, h, b)
    yb2 = rk4_system(f, a, alpha, s2, h, b)

    iter_count = 0
    while abs(yb2 - beta) > tol:
        s_new = s2 - (yb2 - beta) * (s2 - s1) / (yb2 - yb1)
        s1, yb1 = s2, yb2
        s2 = s_new
        yb2 = rk4_system(f, a, alpha, s2, h, b)
        iter_count += 1

        if iter_count > 100:
            raise Exception("Shooting method did not converge")

    print(f"Converged in {iter_count} iterations with slope: {s2:.6f}")
    return s2

# Example BVP: y'' = -y, y(0)=0, y(pi/2)=1
from math import pi

a = 0
b = pi / 2
alpha = 0
beta = 1
h = 0.1

# Initial guesses for y'(0)
s1 = 0.0
s2 = 2.0

# Find correct initial slope
s_correct = shooting_method(f, a, b, alpha, beta, s1, s2, h)

# Solve and print full solution (optional)
def full_solution(f, a, alpha, slope, h, b):
    x_vals = [a]
    y_vals = [alpha]
    x = a
    y1 = alpha
    y2 = slope
    while x < b:
        k1 = h * y2
        l1 = h * f(x, y1, y2)

        k2 = h * (y2 + l1 / 2)
        l2 = h * f(x + h / 2, y1 + k1 / 2, y2 + l1 / 2)

        k3 = h * (y2 + l2 / 2)
        l3 = h * f(x + h / 2, y1 + k2 / 2, y2 + l2 / 2)

        k4 = h * (y2 + l3)
        l4 = h * f(x + h, y1 + k3, y2 + l3)

        y1 += (k1 + 2*k2 + 2*k3 + k4) / 6
        y2 += (l1 + 2*l2 + 2*l3 + l4) / 6
        x += h

        x_vals.append(x)
        y_vals.append(y1)

    return x_vals, y_vals

x, y = full_solution(f, a, alpha, s_correct, h, b)

# Print result
print("\nFinal Solution:")
for xi, yi in zip(x, y):
    print(f"x = {xi:.3f}, y = {yi:.5f}")
