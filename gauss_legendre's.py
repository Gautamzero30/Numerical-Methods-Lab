import  as np

# Function to integrate
def f(x):
    return 1 / (1 + x**2)  # Example: ∫ from 0 to 1 of 1 / (1 + x^2)

def gauss_legendre(f, a, b, n):
    # Get Gauss-Legendre nodes and weights on [-1, 1]
    [x, w] = np.polynomial.legendre.leggauss(n)
    
    # Change of interval from [-1,1] to [a,b]
    t = 0.5 * (x + 1) * (b - a) + a  # transformed nodes
    ft = f(t)
    
    integral = 0.5 * (b - a) * np.dot(w, ft)
    
    return integral

# Example usage
a = 0
b = 1
n = 4  # Number of points

result = gauss_legendre(f, a, b, n)
print(f"Result using {n}-point Gauss-Legendre Quadrature: {result:.10f}")
