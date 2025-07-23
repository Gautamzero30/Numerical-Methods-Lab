def f(x, y):
    return x + y

# Initial conditions
x0 = 0
y0 = 1
h = 0.1
xn = 0.1  # Final x

# Number of steps
n = int((xn - x0)/h)

# Euler's method loop
x = x0
y = y0

for i in range(n):
    y = y + h * f(x, y)
    x = x + h

# Display result
print("Approximate value of y at x = 0.1 is:", y)
