# Victor Zhang, August 6, 2018
# Reading data from the LabJack U3-Lv
# Python

import u3

d = u3.U3() 
d.getCalibrationData()
numsamples = 500
i=0
fileName = 'testSignalGenData.dat'

file = open(fileName, 'w')
file.write("voltage,\n")

while i<numsamples:
    voltageBits, = d.getFeedback(u3.AIN(0)) 
    print(voltageBits)
    voltage = d.binaryToCalibratedAnalogVoltage(voltageBits, isLowVoltage = False, channelNumber = 0)
    print(voltage)
    file.write("{:10.7f},\n".format(voltage))
    i+=1

'''
d.configIO(FIOAnalog = 0, EIOAnalog =0) # configures the FIOs and EIOs to digital
state0 = d.getFIOState(0) # gives 0; means on?
state1 = d.getFIOState(1) # gives 1; means off?
state4 = d.getFIOState(4)

print("state0: %s", state0)
print("state1: %s", state1)
print("state4: %s", state4)
'''
file.close()
d.close() # close the Lab Jack
print("end")
