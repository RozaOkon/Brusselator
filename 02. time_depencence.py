from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import main

a, b = 0, 50
t = np.linspace(a, b, 1000)

# x(t), y(t) plots
sol = solve_ivp(main.brusselator, [a, b], [1, 1])
plt.plot(sol.t, sol.y[0], label = "x(t)")
plt.plot(sol.t, sol.y[1], label = "y(t)")
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.title('Time dependence of x and y intermediates')
plt.show()
