import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(360, step=10)
y = np.sin(x * 2 * np.pi / 360)

f = plt.figure()
ax = plt.axes()
line, = ax.plot(x, y)

def animate(k):
    line.set_data(x[:k], y[:k])

    return line,

anim = FuncAnimation(fig=f, func=animate, interval=20, frames=len(x))

anim.save('animated_image.gif', writer='imagemagick', fps=30)

plt.show()
