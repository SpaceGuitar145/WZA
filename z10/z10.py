import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

y_val = np.linspace(-2, 2, 1000)
z_val = np.linspace(-2, 2, 1000)
y_val, z_val = np.meshgrid(y_val, z_val)

x = y_val * z_val
y = y_val
z = z_val ** 2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('Whitneys Umbrella')
plt.savefig("./whitney_umbrella.png")
