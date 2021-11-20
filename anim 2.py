from skimage.io import imread as imr
from skimage.exposure import rescale_intensity
from matplotlib import pyplot as plt
import numpy as np 
from skmpe import parameters, mpe, OdeSolverMethod


from pylab import *
from matplotlib.animation import FuncAnimation

image = imr('_static/maze.png', as_gray=True).astype(np.float_)
speed_image = rescale_intensity(image, out_range=(0.005, 1.0))

start_point = (60, 238)
end_point = (621, 728)

with parameters(ode_solver_method=OdeSolverMethod.LSODA, integrate_max_step=1.0):
    path_info = mpe(speed_image, start_point, end_point)

path = path_info.path



fig = plt.figure(figsize=(8,6), dpi=150)
plt.imshow(image, cmap='gray')
plt.plot(path[:, 1], path[:, 0], '-r', linewidth=1)

plt.plot(*start_point[::-1], 'oy')
plt.plot(*end_point[::-1], 'og')


x = np.linspace(-2, 4.5, 250) #cree un tableau rempli de 250 valeurs de -2 a 4.5



#trace ligne de separation 
h=1
a=1
b=3

hlines(y=h, xmin=a, xmax=b, linewidth=1.5)
vlines(x=a, ymin=0, ymax=h, linewidth=1.5)
vlines(x=b, ymin=0, ymax=h, linewidth=1.5)

ylim(0,800)
xlim(0,800)
grid()

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


# create a point in the axes
point, = ax.plot(0,1, marker="o")

# Updating function, to be repeatedly called by the animation
def update(i):
    # obtain point coordinates 
    x = path[i][1]
    y = path[i][0]
    # set point's coordinates
    point.set_data([x],[y])
    return point,

# create animation with 10ms interval, which is repeated,
# provide the full path
ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,frames=len(path))


plt.show()