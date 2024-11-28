import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t')
x_expr = (1 - t**2) / (1 + t**2)
y_expr = (2 * t) / (1 + t**2)

x_eq = x_expr**2
y_eq = y_expr**2

sum_eq = sp.simplify(x_eq + y_eq)

simplified_eq = sp.simplify(sum_eq)

circle_eq = sp.Eq(x_expr**2 + y_expr**2, 1)

is_equal = sp.simplify(simplified_eq - 1)

print("Simplified implicit equation:", simplified_eq)
print("Unit circle equation:", circle_eq)
print("Difference between derived implicit equation and unit circle equation:", is_equal)

t_vals = np.linspace(-500, 500, 10000)
x_vals = [(1 - val**2) / (1 + val**2) for val in t_vals]
y_vals = [(2 * val) / (1 + val**2) for val in t_vals]

fig, ax = plt.subplots()

ax.plot(x_vals, y_vals, label='Parametric Curve')

theta = np.linspace(0, 2 * np.pi, 500)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
ax.plot(x_circle, y_circle, label='Implicit Equation (Unit Circle)', linestyle='dashed')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Parametric Curve and Unit Circle')
ax.legend()
ax.grid(True)

plt.axis('equal')  
plt.savefig("./circles.png")
