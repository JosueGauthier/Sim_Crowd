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
print(path[0,0])

print(path[:])
