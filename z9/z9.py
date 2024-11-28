import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, lambdify

x, y = symbols('x y')

eq1 = (x**2 + y**2 + 4*y)**2 - 16*(x**2 + y**2)
eq2 = 2*(x**2 + 9)*(y**2 - 16) + (x**2 - 9)**2 + (y**2 - 16)**2
eq3 = 350*x**2*y**2 - 15**2*(x**2 + y**2) + 12**2*(x**4 + y**4) + 81

def plot_implicit_eq(eq, ax, title):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    f = lambdify((x, y), eq, 'numpy')
    Z = f(X, Y)
    ax.contour(X, Y, Z, levels=[0], colors='blue')
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

plot_implicit_eq(eq1, axs[0], 'Equation 1')
plot_implicit_eq(eq2, axs[1], 'Equation 2')
plot_implicit_eq(eq3, axs[2], 'Equation 3')

plt.tight_layout()
plt.savefig('./equations.png')

def find_singular_points(eq):
    dx = eq.diff(x)
    dy = eq.diff(y)
    solutions = solve((dx, dy), (x, y))
    return solutions

singular_points_eq1 = find_singular_points(eq1)
singular_points_eq2 = find_singular_points(eq2)
singular_points_eq3 = find_singular_points(eq3)

print("Singular points of Equation 1:", singular_points_eq1)
print("Singular points of Equation 2:", singular_points_eq2)
print("Singular points of Equation 3:", singular_points_eq3)
