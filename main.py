import ActuatorComm
import trajectoryGenerator
import time

def collect_dataSet():
    time.sleep(1)
    for k,v in enumerate(trajectoryGenerator.trajectoeies):
        if k != len(trajectoryGenerator.trajectoeies) - 1:
            trajectoryGenerator.trajectory_interpolator(v,trajectoryGenerator.trajectoeies[k+1],8,2)

ActuatorComm.init()

while (True):
    command = input("issue your cmmand my lord>> :D __DELI__")
    if command == 'c':
        collect_dataSet()