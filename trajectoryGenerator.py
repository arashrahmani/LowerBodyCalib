import ActuatorComm
import numpy as np
import math
import time

#   2,	     --Head
#   4,	     --LArm
#   6,7,8,9, --LLeg ( yaw , hip roll , -hip pitch , knee pitch )
#   12,13,16,--RLeg
#   18,19,20,--RArm

trajectoeies = []
trajectoeies.append(np.asarray([0., 0., 90.,  8., -30., -0.,  0., -0.,  0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]))
trajectoeies.append(np.asarray([0., 0., 90.,  8., -30., -0.,  0., -40.,40., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]))
trajectoeies.append(np.asarray([0., 0., 90.,  8., -30., -0.,  0., -40.,  0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]))
# T3 = [0., 0., 90.,  8., -30., -0.,  0., -0., 0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]
# T4 = [0., 0., 90.,  8., -30., -0.,  0., -0., 0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]
# T5 = [0., 0., 90.,  8., -30., -0.,  0., -0., 0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]
# T6 = [0., 0., 90.,  8., -30., -0.,  0., -0., 0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]
# T7 = [0., 0., 90.,  8., -30., -0.,  0., -0., 0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]
# T8 = [0., 0., 90.,  8., -30., -0.,  0., -0., 0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]
# T9 = [0., 0., 90.,  8., -30., -0.,  0., -0., 0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]
# T10 = [0., 0., 90.,  8., -30., -0.,  0., -0., 0., -0., 0., -0.,  0., -0., 0.,-0, 0., 90., -8., -30.]

def trajectory_interpolator(start_state,end_state,n_steps,wait_time):
    step_size =  (end_state - start_state) / n_steps
    print('step_size : ',step_size)
    for k in range(n_steps):
        start_state = start_state + step_size
        print('start_state : ',start_state) 
        ActuatorComm.set_command(start_state*math.pi/180)
        time.sleep(wait_time)