import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 1000)

r = np.sin(2 * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Lemniscate of Bernoulli')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal') 

plt.savefig('./lemniscate.png')
