import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# V(z - x^2 - y^2)
z1 = np.sqrt(x**2 + y**2)

# V(z^2 - x^2 - y^2)
z2_positive = np.sqrt(x**2 + y**2)
z2_negative = -z2_positive

# V(z - x^2 + y^2)
z3 = x**2 - y**2

# V(x, y)
z4 = np.zeros_like(x)

# Create subplots
fig = plt.figure(figsize=(12, 12))

# Plot the first variety
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(x, y, z1, cmap='viridis')
ax1.set_title('V(z - x^2 - y^2)')

# Plot the second variety
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(x, y, z2_positive, cmap='viridis')
ax2.plot_surface(x, y, z2_negative, cmap='viridis')
ax2.set_title('V(z^2 - x^2 - y^2)')

# Plot the third variety
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(x, y, z3, cmap='viridis')
ax3.set_title('V(z - x^2 + y^2)')

# Plot the fourth variety
ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(x, y, z4, cmap='viridis')
ax4.set_title('V(x, y)')

plt.savefig('./varieties.png')