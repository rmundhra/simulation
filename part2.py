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
    yvel:float

time_step = 0.1

def step (state:State) -> State:
    stiffness = 3600
    mass_car = 300
    speed = 15
    driver_input = 0
    if state.time <=3:
        driver_input = state.time/3
    #3+7 = 10
    elif state.time <= 10:
        driver_input = 1.0
    else:
        driver_input  = 0.0
    

    angle = 5*driver_input
    steer_angle = np.radians(angle)
    slip_angle = steer_angle - (state.yvel/speed)
    lateral_force = stiffness + slip_angle
    lateral_acceleration = lateral_force/mass_car

    new_yvel = state.yvel + lateral_acceleration*time_step
    new_xpos = state.xpos + speed*time_step
    new_ypos = state.ypos + state.yvel*time_step
    new_time = state.time + time_step


    newState = State(

    xvel = speed,
    xpos = new_xpos,
    ypos = new_ypos,
    time = new_time,
    yvel = new_yvel,
   
    )

    return newState

s0 = State(xvel=0, xpos=0, ypos=0, time=0, yvel=0)
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