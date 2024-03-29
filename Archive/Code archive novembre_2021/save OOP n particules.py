from skimage.io import imread as imr
from skimage.exposure import rescale_intensity
from matplotlib import pyplot as plt
import numpy as np 
from skmpe import parameters, mpe, OdeSolverMethod

import random as rd

from pylab import *
from matplotlib.animation import FuncAnimation


class Particle:
    """A class representing a two-dimensional particle."""

    def __init__(self, x, y,path):
        """Initialize the particle's position, velocity, and radius."""

        self.coord = np.array((x, y))
        self.path_p = path

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
 
class Simulation:
    """A class for a simulation of n people try to escape the maze/room/building"""

    ParticleClass = Particle

    def calc_chemin(self,speed_image,start_point,end_point):

        with parameters(ode_solver_method=OdeSolverMethod.LSODA, integrate_max_step=1.0):
            path_info = mpe(speed_image, start_point, end_point)
        return path_info.path

    def creation_plot(self,image_brute,start,start_type,end_point,nparticles):

        image = imr(image_brute, as_gray=True).astype(np.float_)
        speed_image = rescale_intensity(image, out_range=(0.005, 1.0))

        fig = plt.figure(figsize=(8,6), dpi=150)
        plt.imshow(image, cmap='gray')

        particule=[]

        for particule_i in range(nparticles):

            if start_type == "point":
                start_point = start

            if start_type =="zone":
                abs = rd.randint(start[0][0],start[0][1])
                ord = rd.randint(start[1][0],start[1][1])
                start_point =(abs,ord)

            if start_type == "alea":
                abs = rd.randint(0,749)
                ord = rd.randint(0,749)
                start_point =(abs,ord)
            
            pathCP = self.calc_chemin(speed_image,start_point,end_point)
            p = Particle(start_point[0],start_point[1],pathCP)
            particule.append(p)
            plt.plot(pathCP[:, 1], pathCP[:, 0], '-r', linewidth=1)
            plt.plot(*start_point[::-1], 'oy')
            plt.plot(*end_point[::-1], 'og')
  
    
        ylim(0,800)
        xlim(0,800)
        grid()

        return fig,particule

    def moving_point(self,fig,particule,nparticule) :

        point_list=[]
        
        for i in range(nparticule):
            ax = gca()
            # create a point in the axes
            point_list.append(ax.plot(0,1, marker="o"))


        return point_list
        


    def do_animation(self):
        """Set up and carry out the animation."""

        #set up anim
        fig,particule = self.creation_plot(image_brute,start,start_type,end_point,nparticles)
        point_list = self.moving_point(fig,particule,nparticles)


        # Updating function, to be repeatedly called by the animation
        # create animation with 10ms interval, which is repeated,
        # provide the full path
        
        anim = FuncAnimation(fig, self.animate, interval=10, blit=True, repeat=True,frames=600)
        #anim = animation.FuncAnimation(self.fig, self.animate,init_func=self.init, frames=1000, interval=interval, blit=True)
        

        plt.show()
    
    def animate(self, i):
        """The function passed to Matplotlib's FuncAnimation routine."""

        self.update()
        print(self.circles)
        return self.circles

    def update(self,i):
        # obtain point coordinates 
        for particule_i in range(nparticles):

            particule[particule_i].x= particule[particule_i].path_p[i][1]
            particule[particule_i].y= particule[particule_i].path_p[i][0]
            print(particule[particule_i].x)

            print("aa")
            # set point's coordinates
            point_list[particule_i][0].set_data(particule[particule_i].x,particule[particule_i].y)
        print(point_list[0][0])
        print(point_list[1][0])
        print(point_list)
        
        return 
    
    
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
