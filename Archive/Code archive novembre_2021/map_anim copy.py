import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from scipy.misc import imread

from matplotlib.pyplot import imread


img = imread("usamap.jpg")

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 20), ylim=(0, 20))

plt.imshow(img,zorder=0,  extent=[0.1, 20.0, 0.1, 20.0])
plt.show()