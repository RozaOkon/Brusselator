from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import math

A, B = 1, 3
w = 0.2
e = 0.2


def brusselator(t, x):
    return A + 2 * x * x - (B + 1) * x + e * math.cos(w * t)

def brusselator_mod(t, x):
    return A_mod + 2 * x * x - (B_mod + 1) * x + e * math.cos(w_1 * t)


e_list = np.linspace(0, 10000, 50)
t = 14
x_list = []
x_mod_list = []

a, b = 1, 10
t = np.linspace(a, b, 10)
step = 0.5

for j in range (0, 10):
    for i in e_list:
        def brusselator(t, x):
            return A + 2 * x * x - (B + 1) * x + i * math.cos(w * t)
        sol = solve_ivp(brusselator, [a, b], [1 + j * step, 1 + j * step])
        x_list.append(sol.y[0, 10])
    plt.plot(e_list, x_list, "o", linewidth = 0.5, markersize = 3, label = str(j))
    x_list = []
plt.legend()
plt.xlabel("e parameter")
plt.ylabel("[X]")
plt.show()
