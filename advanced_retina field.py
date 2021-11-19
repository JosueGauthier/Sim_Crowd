from skimage.data import retina
from skimage.color import rgb2gray
from skimage.transform import rescale
from skimage.filters import sato

from matplotlib import pyplot as plt

image_data = rescale(rgb2gray(retina()), 0.5)
speed_data = sato(image_data) + 0.05
speed_data[speed_data > 1.0] = 1.0

_, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(image_data, cmap='gray')
ax1.set_title('source data')
ax1.axis('off')
ax2.imshow(speed_data, cmap='gray')
ax2.set_title('speed data')
ax2.axis('off')





from skmpe import mpe
import numpy as np 

# define starting and ending points
start_point = (165, 280)
end_point = (611, 442)

path_info = mpe(speed_data, start_point, end_point)

# get computed travel time for given ending point and extracted path
travel_time = path_info.pieces[0].travel_time
path = path_info.path

nrows, ncols = speed_data.shape
xx, yy = np.meshgrid(np.arange(ncols), np.arange(nrows))

fig, ax = plt.subplots(1, 1)
ax.imshow(speed_data, cmap='gray', alpha=0.9)
ax.plot(path[:,1], path[:,0], '-', color=[0, 1, 0], linewidth=2)
ax.plot(start_point[1], start_point[0], 'or')
ax.plot(end_point[1], end_point[0], 'o', color=[1, 1, 0])
tt_c = ax.contour(xx, yy, travel_time, 20, cmap='plasma', linewidths=1.5)
ax.clabel(tt_c, inline=1, fontsize=9, fmt='%d')
ax.set_title('travel time contours and minimal path')
ax.axis('off')
cb = fig.colorbar(tt_c)
cb.ax.set_ylabel('travel time')

plt.show()