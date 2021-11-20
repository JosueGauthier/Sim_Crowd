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

start_point2 = (72, 537)

class Particle:
    pass

class Simulation:
    """A class for a simulation of n people try to escape the maze.
    """

    ParticleClass = Particle

    def __init__(self, n):
        """Initialize the simulation with n Particles.
        """

        self.init_particles(n)

    def place_particle(self):
        """Place x, y so that the Particle is entirely inside the domain of the simulation."""
    
        x= start_point[0]
        y= start_point[1]

    def init(self):
        """Initialize the Matplotlib animation."""

        self.circles = []
        for particle in self.particles:
            self.circles.append(particle.draw(self.ax))
        return self.circles

    def animate(self, i):
        """The function passed to Matplotlib's FuncAnimation routine."""

        self.advance_animation()
        return self.circles

    def setup_animation(self):
        """
        self.fig, self.ax = plt.subplots()
        for s in ['top','bottom','left','right']:
            self.ax.spines[s].set_linewidth(2)
        self.ax.set_aspect('equal', 'box')
        self.ax.set_xlim(0, globalxlim)
        self.ax.set_ylim(0, globalylim)
        self.ax.xaxis.set_ticks([])
        self.ax.yaxis.set_ticks([])

        """

    def do_animation(self):
        """Set up and carry out the animation.
        """

        self.setup_animation()
        anim = animation.FuncAnimation(self.fig, self.animate,
                init_func=self.init, frames=1, interval=1, blit=True)
    


if __name__ == '__main__':

    nparticles = 2
    raddi = 10 #raddius of particle
    styles = {'edgecolor': 'red','facecolor': 'red', 'linewidth': 0, 'fill':True }
    
    sim = Simulation(nparticles)
    sim.do_animation()

def calc_chemin():
    with parameters(ode_solver_method=OdeSolverMethod.LSODA, integrate_max_step=1.0):
        path_info = mpe(speed_image, start_point, end_point)
    return path_info.path

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