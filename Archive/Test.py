from skimage.io import imread as imr
from skimage.exposure import rescale_intensity
from matplotlib import pyplot as plt
import numpy as np 
from skmpe import parameters, mpe, OdeSolverMethod


from pylab import *
from matplotlib.animation import FuncAnimation

import random as rd
n = 5
radius = 2

# class Point:
#     "Definition d'un point geometrique"

# p = Point()
# p.x = 1
# p.y = 2
# print("p : x =", p.x, "y =", p.y)


class Particle:
    """A class representing a two-dimensional particle."""

    def __init__(self, x, y):
        """Initialize the particle's position, velocity, and radius."""

        self.coord = np.array((x, y))

    @property
    def x(self):
        return self.coord[0]
    @x.setter
    def x(self, value):
        self.coord[0] = value
    @property
    def y(self):
        return self.coord[1]
    @y.setter
    def y(self, value):
        self.coord[1] = value

p = Particle(1,2)

print(p)

print(p.x)