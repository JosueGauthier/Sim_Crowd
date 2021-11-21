from skimage.io import imread as imr
from skimage.exposure import rescale_intensity
from matplotlib import pyplot as plt
import numpy as np 
from skmpe import parameters, mpe, OdeSolverMethod


from pylab import *
from matplotlib.animation import FuncAnimation



ax = gca()
# create a point in the axes
point, = ax.plot(0,1, marker="o")

print(ax.plot(0,1, marker="o"))
print(point,)