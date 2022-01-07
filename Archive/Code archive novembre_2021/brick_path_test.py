from skimage.data import brick
from skimage.transform import rescale
from skimage.exposure import rescale_intensity, adjust_sigmoid

from matplotlib import pyplot as plt
import numpy as np


from skmpe import parameters, mpe

image = rescale(brick(), 0.5)
speed_image = rescale_intensity(
    adjust_sigmoid(image, cutoff=0.5, gain=10).astype(np.float_), out_range=(0., 1.))

start_point = (44, 13)
end_point = (233, 230)
way_points = [(211, 59), (17, 164)]

with parameters(integrate_max_step=1.0):
    path_info1 = mpe(speed_image, start_point, end_point)
    path_info2 = mpe(speed_image, start_point, end_point, way_points)

px1, py1 = path_info1.path[:, 1], path_info1.path[:, 0]
px2, py2 = path_info2.path[:, 1], path_info2.path[:, 0]

plt.imshow(image, cmap='gray')
plt.plot(px1, py1, '-r', linewidth=2)
plt.plot(px2, py2, '--r', linewidth=2)

plt.plot(*start_point[::-1], 'oy')
plt.plot(*end_point[::-1], 'og')
for p in way_points:
    plt.plot(*p[::-1], 'ob')
plt.axis('off')

plt.show()