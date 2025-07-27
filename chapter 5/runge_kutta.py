def runge_kutta_2(f, x0, y0, xn, h):
    x = x0
    y = y0
    n = int((xn - x0) / h)

    print("\nStep\t x\t\t y")
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y += 0.5 * (k1 + k2)
        x += h
        print(f"{i:2d}\t {x:.5f}\t {y:.5f}")

    return y

# Example differential equation: dy/dx = x + y
def f(x, y):
    return x + y

# Initial conditions
x0 = 0
y0 = 1
xn = 1
h = 0.1

print("Solving dy/dx = x + y using 2nd Order Runge-Kutta Method")
final_y = runge_kutta_2(f, x0, y0, xn, h)
print(f"\nFinal value at x = {xn} is y = {final_y:.5f}")
