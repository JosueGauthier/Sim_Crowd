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

start_point2 = (72, 537)



with parameters(ode_solver_method=OdeSolverMethod.LSODA, integrate_max_step=1.0):
    path_info = mpe(speed_image, start_point, end_point)

with parameters(ode_solver_method=OdeSolverMethod.LSODA, integrate_max_step=1.0):
    path_info2 = mpe(speed_image, start_point2, end_point)

path = path_info.path

path2 = path_info2.path



#fig = plt.figure(figsize=(8,6), dpi=150)
fig = plt.figure(dpi=150)

plt.imshow(image, cmap='gray')
plt.plot(path[:, 1], path[:, 0], '-r', linewidth=1)

plt.plot(*start_point[::-1], 'oy')
plt.plot(*end_point[::-1], 'og')


plt.plot(path2[:, 1], path2[:, 0], '-y', linewidth=1)

plt.plot(*start_point2[::-1], 'oc')
plt.plot(*end_point[::-1], 'om')


ylim(0,800)
xlim(0,800)
grid()

ax = gca()


# create a point in the axes
point, = ax.plot(0,1, marker="o")

point2, = ax.plot(0,1, marker="o")

# Updating function, to be repeatedly called by the animation
def update(i):
    # obtain point coordinates 
    x = path[i][1]
    y = path[i][0]
    x2 = path2[i][1]
    y2 = path2[i][0]


    # set point's coordinates
    point.set_data([x],[y])

    point2.set_data([x2],[y2])

    print(point,point2)
    return point,point2,

# create animation with 10ms interval, which is repea ted,
# provide the full path
ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,frames=len(path))


plt.show()