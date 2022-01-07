from skimage.io import imread
from skimage.exposure import rescale_intensity

from matplotlib import pyplot as plt

import numpy as np 
from skmpe import parameters, mpe, OdeSolverMethod

image = imread('_static/maze.png', as_gray=True).astype(np.float_)
speed_image = rescale_intensity(image, out_range=(0.005, 1.0))

start_point = (60, 238)
#print(start_point[0])
end_point = (621, 728)

with parameters(ode_solver_method=OdeSolverMethod.LSODA, integrate_max_step=1.0):
    path_info = mpe(speed_image, start_point, end_point)

path = path_info.path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 3*np.pi
w = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151

x = np.linspace(xmin, xmax, nbx)

fig = plt.figure() # initialise la figure
line, = plt.plot([], []) 
plt.xlim(xmin, xmax)
plt.ylim(-1, 1)

def animate(i): 
    t = i * dt
    y = np.cos(k*x - w*t)
    line.set_data(x, y)
    return line,
 
ani = animation.FuncAnimation(fig, animate, frames=4000, blit=True, interval=100, repeat=False)

plt.show()



