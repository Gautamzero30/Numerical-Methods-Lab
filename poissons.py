import numpy as np
import matplotlib.pyplot as plt

nx, ny = 50, 50
max_iter = 500
u = np.zeros((ny, nx))

f = np.zeros((ny, nx))
f[ny//2, nx//2] = 100  # source in center

h = 1
for _ in range(max_iter):
    u[1:-1, 1:-1] = 0.25 * (u[1:-1, :-2] + u[1:-1, 2:] +
                            u[:-2, 1:-1] + u[2:, 1:-1] - h**2 * f[1:-1, 1:-1])

plt.imshow(u, cmap='hot', origin='lower')
plt.colorbar(label='Potential')
plt.title("Poisson's Equation Solution")
plt.show()
