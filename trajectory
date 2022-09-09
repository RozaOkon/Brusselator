from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import main

a, b = 0, 50
t = np.linspace(a, b, 1000)

for x0 in range(0, 6):
    for y0 in [0, 3]:
        sol = solve_ivp(main.brusselator, [a, b], [x0, y0])
        plt.plot(sol.y[0], sol.y[1], ":", color="blue")
        plt.xlabel('[X]')
        plt.ylabel('[Y]')
plt.title('Trajectory of Brusselator')
plt.show()
