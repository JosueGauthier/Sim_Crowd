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

    def creation_plot(self,speed_image,start_point,end_point):

        fig = plt.figure(figsize=(8,6), dpi=150)
        plt.imshow(image, cmap='gray')
        pathCP = self.calc_chemin(speed_image,start_point,end_point)
        plt.plot(pathCP[:, 1], pathCP[:, 0], '-r', linewidth=1)

        plt.plot(*start_point[::-1], 'oy')
        plt.plot(*end_point[::-1], 'og')


        ylim(0,800)
        xlim(0,800)
        grid()

        plt.show()

    def __init__(self, n):
        """Initialize the simulation with n Particles.
        """
        pass
        
        """    
        fig = plt.figure(figsize=(8,6), dpi=150)
        plt.imshow(image, cmap='gray')
        plt.plot(path[:, 1], path[:, 0], '-r', linewidth=1)

        plt.plot(*start_point[::-1], 'oy')
        plt.plot(*end_point[::-1], 'og')


        ylim(0,800)
        xlim(0,800)
        grid()

        plt.show()

        """

    def do_animation(self):

        pass 
        self.creation_plot(speed_image,start_point,end_point)
        """Set up and carry out the animation.
        """
        """
        self.setup_animation()
        anim = animation.FuncAnimation(self.fig, self.animate,
                init_func=self.init, frames=1, interval=1, blit=True)

        """
    


if __name__ == '__main__':

    nparticles = 2
    raddi = 10 #raddius of particle
    styles = {'edgecolor': 'red','facecolor': 'red', 'linewidth': 0, 'fill':True }
    
    sim = Simulation(nparticles)

    a=sim.calc_chemin(speed_image,start_point,end_point)

    print(a)

    sim.do_animation()



"""

fig = plt.figure(figsize=(8,6), dpi=150)
plt.imshow(image, cmap='gray')
plt.plot(path[:, 1], path[:, 0], '-r', linewidth=1)

plt.plot(*start_point[::-1], 'oy')
plt.plot(*end_point[::-1], 'og')


ylim(0,800)
xlim(0,800)
grid()

plt.show()

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
    return point,point2,

# create animation with 10ms interval, which is repeated,
# provide the full path
ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,frames=len(path))


plt.show()

"""