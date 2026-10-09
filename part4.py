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

    max_prop = 2000
    vmax = 27
    mass = 300
    
    mass_car = 300

    driver_input = 0
    if state.time <=3:
        driver_input = state.time/3
    #3+7 = 10
    else:
        driver_input  = 1.0

    
    prop = max_prop * driver_input * (1 - (state.xvel/vmax))
    acc = prop/mass_car
    new_xvel = state.xvel+(acc*time_step)
    new_xpos = state.xpos+state.xvel*time_step
    new_time = state.time+time_step

    return State(xvel = new_xvel,
    xpos = new_xpos,
    ypos = 0,
    time = new_time)



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