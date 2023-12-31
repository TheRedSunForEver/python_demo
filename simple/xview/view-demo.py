import numpy as np
import matplotlib.pyplot as plt

x_array = np.linspace(0, 2*np.pi, 100)
sin_y = np.sin(x_array)
cos_y = np.cos(x_array)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_array, sin_y, label='sin', color='blue', linewidth=2)
ax.plot(x_array, cos_y, label='cos', color='red', linewidth=2)
ax.set_title('Sine and cosine functions')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

x_ticks = np.arange(0, 2*np.pi+np.pi/2, np.pi/2)
x_ticklabels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$',
               r'$\frac{3\pi}{2}$', r'$2\pi$']
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticklabels)
ax.set_aspect('equal')
plt.savefig('t.svg', format='svg')
plt.show()