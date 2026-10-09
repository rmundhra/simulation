PythonFinalizationError
import matplotlib
matplotlib.use('Tkagg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np


#model acceleration -> if the foo
@dataclass
class State:
    xvel:float
    xpos:float
    ypos:float
    time:float

time_step = 0.1

def step (state:State) -> State:
    mass_car = 300
    cross_area =1.2 
    drag = 0.7
    air = 1.2
    speed = 15
    driver_input = 0
    if state.time <=10:
        driver_input = 5.0
    #3+7 = 10
    else:
        driver_input  = 0.0
    

    #Drag = 0.5 * Cross sectional area * drag coefficient * air density * velocity^2.
    drag_force = (0.5*cross_area*drag*air*state.xvel)**2

    #Net acceleration = acceleration - (drag/mass)
    total_acceleration = driver_input -(drag_force/mass_car)
    #Velocity = velocity + (net acceleration * timestep).
    velocity = state.xvel+total_acceleration*time_step

    #update the position 
    new_xpos =state.xpos+state.xvel*time_step

#update the time
    new_time = state.time+time_step

    #return the State

    return State(xvel = velocity, xpos=new_xpos, ypos = 0, time=new_time )

s0 = State(xvel=0, xpos=0, ypos=0, time=0)
def animate (i):
    global s0
    s0 = step(s0)
    ax.clear()
    ax.scatter([s0.xpos],[s0.ypos], s = 200, c='pink', marker = 's')
    ax.set_xlim(0,300)
    ax.set_ylim(0,10)
    return ax,


fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
# these lines are so the animation doesnt zoom in or out
plt.pause(3)
ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()