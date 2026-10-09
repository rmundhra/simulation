#add rolling resistance 
PythonFinalizationError
import matplotlib
matplotlib.use('Tkagg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np


@dataclass
class State:
    xvel:float
    xpos:float
    ypos:float
    time:float

time_step = 0.1

def step (state:State) -> State:

    break_capacity = 1850
    mass_car = 300
    driver_input = 0
    rolling_resistance = 0.018

    if state.time<=2:
        driver_input = 0.0
    else:
        driver_input = 1.0

    rolling_force = rolling_resistance*mass_car*9.81
    breaking_force = driver_input*break_capacity
    acceleration = -((breaking_force+rolling_force)/mass_car)
    new_velocity = state.xvel + acceleration*time_step

    if new_velocity<0:
        new_velocity = 0
    new_xpos = state.xpos + state.xvel*time_step
    new_time = state.time + time_step
    return State(xvel = new_velocity,xpos = new_xpos,ypos = 0,time = new_time)


s0 = State(xvel=50, xpos=0, ypos=0, time=0)
times = []
times.append(s0.time)
velocity= []
velocity.append(s0.xvel)
def animate (i):
    global s0
    s0 = step(s0)
    ax.clear()
    ax.scatter([s0.xpos],[s0.ypos], s = 200, c='pink', marker = 's')
    ax.set_xlim(0,300)
    ax.set_ylim(0,10)
    times.append(s0.time)               
    velocity.append(s0.xvel)              
    ax2.clear()                          
    ax2.plot(times, velocity, color='m')     
    ax2.set_xlim(0,15)                  
    ax2.set_ylim(0,60)                  
    ax2.set_xlabel("time(s)")            
    ax2.set_ylabel("velocity (m/s)")      
    return ax,


fig = plt.figure()
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)




ax.grid()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
plt.pause(3)
ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()