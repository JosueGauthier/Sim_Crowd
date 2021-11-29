from skimage.io import imread
from skimage.exposure import rescale_intensity

from matplotlib import pyplot as plt

import numpy as np 
from skmpe import parameters, mpe, OdeSolverMethod

image = imread('_static/maze.png', as_gray=True).astype(np.float_)
speed_image = rescale_intensity(image, out_range=(0.005, 1.0))

start_point = (60, 238)
end_point = (621, 728)

with parameters(ode_solver_method=OdeSolverMethod.LSODA, integrate_max_step=1.0):
    path_info = mpe(speed_image, start_point, end_point)

path = path_info.path
print(path[0])




import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
#points, = ax.plot(np.random.rand(10), 'o')
points = 
ax.set_ylim(0, 500)
ax.set_xlim(0, 500)

def update(data):
    points.set_ydata(data)
    return points,

def generate_points():
    while True:
        yield np.random.rand(10)  # change this

ani = animation.FuncAnimation(fig, update, generate_points, interval=300)
ani.save('animation.gif', writer='imagemagick', fps=60);
plt.show()