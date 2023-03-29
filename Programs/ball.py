# Program to calculate the height of a ball in veritcal motion
import numpy as np 
import matplotlib.pyplot as plt


v = 5 #velocity
g = 9.81 #acceleration of gravity
t = np.linspace(0, 1, 1001)

y = v*t - 0.5*g*t**2

plt.plot(t, y)
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.show()
