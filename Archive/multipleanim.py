import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as mat_anim

u = 5                                                                
g = 9.8       
theta_degree = np.rad2deg([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
theta_rad = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2]
fr = 100
print(1)

def projectile_range():
    # calculate projectile range
    rng = ((u**2)*(np.sin(np.multiply(2.0, theta_rad))))/g
    return rng

def max_height():
    # calculate maximum height of projectile
    max_ht = ((u*np.sin(theta_rad))**2)/(2*g)
    return max_ht

y=[]
def projectile():
    # calculating projectile path
    r = projectile_range()
    for j in range(len(r)):
        x = np.linspace(0, r[j], 100)
        y.append(x*(np.tan(theta_rad[j])) - ((0.5*g*(x**2))/(u*np.cos(theta_rad[j]))**2))
    return y

fig1, ax1 = plt.subplots(1,1)
fig1.suptitle("Projectile Motion Range", fontsize = 10)
ax1.set_xlim([0, round(max(projectile_range()))+1])
ax1.set_ylim([0, round(max(max_height()))+1])
# ax_range, = ax1.plot([], [])
dots, = ax1.plot([], [], 'o')
lines, = ax1.plot([], [], lw = 2)

plot_colour = ["black", "red", "green", "yellow", "blue"]
line_list = []
dot_list = []
print(2)
for index in range(len(theta_rad)):
    line_obj = ax1.plot([], [], lw = 2, color = plot_colour[index])[0]
    dot_obj = ax1.plot([], [], 'o', color = plot_colour[len(theta_rad)-index-1])[0]
    line_list.append(line_obj)
    dot_list.append(dot_obj)
print(3)

def initialize():
    # initializing projectile range plot
    print(4)
    for line in line_list:
        line.set_data([], [])
    for dot in dot_list:
        dot.set_data([], [])
    print(5)

    return dot_list, line_list,

print(6)

def proj_animation(i):
    # animation function
    print(7)
    n = 100
    # fr = n
    y = np.empty([len(theta_rad), n], dtype = float)
    x = np.empty([len(theta_rad), n], dtype = float)
    r = projectile_range()
    graph_list = []
    for j in range(len(r)):
        x[j] = np.linspace(0, r[j], n)
        y[j] = np.multiply(x[j], np.tan(theta_rad[j])) - ((0.5*g*(np.square(x[j])))/(u*np.cos(theta_rad[j]))**2)

    for count, element in enumerate(line_list):
        element.set_data(x[count][:i], y[count][:i])

    for count, element in enumerate(dot_list):
        element.set_data(x[count][i], y[count][i])
    
    graph_list.append(dot_list)
    graph_list.append(line_list)
    graph_list = [item for sublist in graph_list for item in sublist] 
    print(8)
    return graph_list

proj_anim = mat_anim.FuncAnimation(fig1, proj_animation, frames = fr,
                                   interval = 20, blit = True)
proj_anim.save("projectile_range.mp4", fps = 20, extra_args = ['-vcodec', 'libx264'])

plt.show()