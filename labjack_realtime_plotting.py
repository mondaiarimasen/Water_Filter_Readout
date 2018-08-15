# Victor Zhang, August 6, 2018
# Reading data from the LabJack U3-Lv
# Python

import u3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

d = u3.U3() 
d.debug = True
print("getCalibrationData:")
print(d.getCalibrationData(),"\n")
print("configIO:")
print(d.configIO(), "\n")
d.configIO(FIOAnalog = 15)
print("configIO:")
print(d.configIO(), "\n")
numsamples = 500
i=0
fileName = 'testSignalGenData.dat'

y = np.zeros(100000)
x = np.arange(100000)

def update(i):
#getAIN seems to be better, since it automatically changes the bits to volt for you
#    voltBits0, = d.getFeedback(u3.AIN(0))
    #voltBits1, = d.getFeedback(u3.AIN(1)) 

    #print("voltBits1 at %s: %s" % (i,voltBits1))
    #volt1 = d.binaryToCalibratedAnalogVoltage(voltBits1, isLowVoltage = False, channelNumber = 0)
    print("voltage at %s: %s vs %s\n" % (i,d.getAIN(1),d.getAIN(0)))
    y[i]=d.getAIN(0)-d.getAIN(1)

    
#file = open(fileName, 'w')
#file.write("voltage,\n")

fig, ax = plt.subplots()
line, = ax.plot([], [], 'k-')
ax.margins(0.05)

def init():
    line.set_data(x[:2],y[:2])
    return line,

def animate(i):
    win = 100
    update(i)
    imin = min(max(0,i - win), len(x) - win)
    xdata = x[imin:i]
    ydata = y[imin:i]
    line.set_data(xdata, ydata)
    ax.relim()
    ax.autoscale()
    print(i)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, interval=100)

plt.show()

'''
while i<numsamples:
    voltageBits, = d.getFeedback(u3.AIN(1,0)) 
    print(voltageBits)
    voltage = d.binaryToCalibratedAnalogVoltage(voltageBits, isLowVoltage = True, isSingleEnded = True, isSpecialSetting = False, channelNumber = 0)
    print(voltage)
    #   print(d.getAIN(0))
    file.write("{:10.7f},\n".format(voltage))
    i+=1


d.configIO(FIOAnalog = 0, EIOAnalog =0) # configures the FIOs and EIOs to digital
state0 = d.getFIOState(0) # gives 0; means on?
state1 = d.getFIOState(1) # gives 1; means off?
state4 = d.getFIOState(4)

print("state0: %s", state0)
print("state1: %s", state1)
print("state4: %s", state4)

file.close()
d.close() # close the Lab Jack
print("end")
'''

d.close()


