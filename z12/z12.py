import matplotlib.pyplot as plt
import numpy as np

def conchoid_curve(a, t):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(np.cos(t) != 0, 1 / np.cos(t) + a * np.cos(t), np.inf)

def plot_conchoid_curves(a_values):
    t = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 1000) 

    plt.figure(figsize=(12, 8))
    for a in a_values:
        r = conchoid_curve(a, t)
        x = r * np.cos(t)
        y = r * np.sin(t)
        plt.plot(x, y, label=f'a = {a}')
    
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Conchoid of Sluse for different values of a')
    plt.legend()
    plt.xlim(-10, 10)  
    plt.ylim(-10, 10) 
    plt.grid(True)
    plt.savefig('./conchoid_curves.png')

a_values = [-4, -2, 0, 1, 2, 3]
plot_conchoid_curves(a_values)
