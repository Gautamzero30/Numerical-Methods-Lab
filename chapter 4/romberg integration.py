import numpy as np

# Function to integrate
def f(x):
    return 1 / (1 + x**2)  # Example: ∫ from 0 to 1 of 1 / (1 + x^2) dx

def romberg(a, b, n):
    R = np.zeros((n, n))
    
    # Trapezoidal approximations
    for i in range(n):
        N = 2**i
        h = (b - a) / N
        sum_ = 0.5 * (f(a) + f(b))
        for k in range(1, N):
            sum_ += f(a + k * h)
        R[i, 0] = h * sum_
    
    # Richardson extrapolation
    for j in range(1, n):
        for i in range(j, n):
            R[i, j] = (4**j * R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

    # Print table
    print("Romberg Integration Table:")
    for i in range(n):
        for j in range(i + 1):
            print(f"{R[i,j]:.10f}", end="\t")
        print()

    return R[n-1, n-1]  # Most accurate result

# Example usage
a = 0.0
b = 1.0
n = 5
result = romberg(a, b, n)
print(f"\nFinal Result = {result:.10f}")
