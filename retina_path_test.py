from matplotlib import pyplot as plt

from skimage.data import retina
from skimage.color import rgb2gray
from skimage.transform import rescale
from skimage.filters import sato

from skmpe import mpe

image = rescale(rgb2gray(retina()), 0.5)
speed_image = sato(image)

start_point = (76, 388)
end_point = (611, 442)
way_points = [(330, 98), (554, 203)]

path_info = mpe(speed_image, start_point, end_point, way_points)

px, py = path_info.path[:, 1], path_info.path[:, 0]

plt.imshow(image, cmap='gray')
plt.plot(px, py, '-r')

plt.plot(*start_point[::-1], 'oy')
plt.plot(*end_point[::-1], 'og')
for p in way_points:
    plt.plot(*p[::-1], 'ob')

plt.show()