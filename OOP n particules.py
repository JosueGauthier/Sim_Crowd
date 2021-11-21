from skimage.io import imread as imr
from skimage.exposure import rescale_intensity
from matplotlib import pyplot as plt
import numpy as np 
from skmpe import parameters, mpe, OdeSolverMethod

import random as rd

from pylab import *
from matplotlib.animation import FuncAnimation


class Particle:
    pass

class Simulation:
    """A class for a simulation of n people try to escape the maze.
    """

    ParticleClass = Particle

    def calc_chemin(self,speed_image,start_point,end_point):

        with parameters(ode_solver_method=OdeSolverMethod.LSODA, integrate_max_step=1.0):
            path_info = mpe(speed_image, start_point, end_point)
        return path_info.path

    def creation_plot(self,image_brute,start,start_type,end_point):



        image = imr(image_brute, as_gray=True).astype(np.float_)
        speed_image = rescale_intensity(image, out_range=(0.005, 1.0))

        fig = plt.figure(figsize=(8,6), dpi=150)
        plt.imshow(image, cmap='gray')

        if start_type == "point":
            start_point = start


        if start_type =="zone":
            abs = rd.randint(start[0][0],start[0][1])
            ord = rd.randint(start[1][0],start[1][1])
            start_point =(abs,ord)


        if start_type == "alea":
            abs = rd.randint(0,800)
            ord = rd.randint(0,800)
            start_point =(abs,ord)


        pathCP = self.calc_chemin(speed_image,start_point,end_point)
        plt.plot(pathCP[:, 1], pathCP[:, 0], '-r', linewidth=1)

        plt.plot(*start_point[::-1], 'oy')
        plt.plot(*end_point[::-1], 'og')


        ylim(0,800)
        xlim(0,800)
        grid()

        return fig,pathCP

    def moving_point(self,fig,path) :

        ax = gca()
        # create a point in the axes
        point, = ax.plot(0,1, marker="o")

        return point


    def do_animation(self):
        """Set up and carry out the animation."""

        #set up anim
        fig,path = self.creation_plot(image_brute,start,start_type,end_point)
        point = self.moving_point(fig,path)

        # Updating function, to be repeatedly called by the animation
        # create animation with 10ms interval, which is repeated,
        # provide the full path

        print(self.nbparticules)


        def update(i):
            # obtain point coordinates 
            x = path[i][1]
            y = path[i][0]

            # set point's coordinates
            point.set_data([x],[y])

            return point,


        anim = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,frames=len(path))

        plt.show()



    def __init__(self,nbparticules):
        """Initialize the simulation with n Particles.
        """
        self.nbparticules = nbparticules


    
if __name__ == '__main__':

    #chemin vers l'image du plan d'evacuation 
    image_brute = '_static/maze.png'

    #si points de departs souhaités
    #start_type ="point"
    #start = (60, 238)

    #si zone de depart souhaitée
    start_type ="zone"
    start=((40,600),(100,200))

    #si repartition alétoire
    #start = None
    #start_type ="alea"
    
    
    end_point = (621, 728)

    nparticles = 2
    raddi = 10 #raddius of particle
    styles = {'edgecolor': 'red','facecolor': 'red', 'linewidth': 0, 'fill':True }
    
    sim = Simulation(nparticles)

    sim.do_animation()
