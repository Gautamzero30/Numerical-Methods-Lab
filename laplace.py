import numpy as np
import matplotlib.pyplot as plt

nx, ny = 50, 50
max_iter = 500
u = np.zeros((ny, nx))

u[:, 0] = 100
u[:, -1] = 100

for _ in range(max_iter):
    u[1:-1, 1:-1] = 0.25 * (u[1:-1, :-2] + u[1:-1, 2:] + u[:-2, 1:-1] + u[2:, 1:-1])

plt.imshow(u, cmap='hot', origin='lower')
plt.colorbar(label='Potential')
plt.title("Laplace's Equation Solution")
plt.show()
