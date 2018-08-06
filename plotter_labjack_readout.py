# Victor Zhang, August 6, 2018
# Plotter for labjack_readout.py (testing signal generator)
# Python

import matplotlib.pyplot as plt
import numpy as np
import csv

fileName = "testSignalGenData.dat"
result = []

with open(fileName,"r") as csvfile:
    reader = csv.reader(csvfile,delimiter = ",")
    next(reader)
    for row in reader:
        result.append(row[0])

print(result)

plt.figure(figsize=(12,8))
plt.plot(list(j for j in range(0,len(result))),[float(i) for i in result])
plt.gcf().autofmt_xdate()
plt.gcf().subplots_adjust(bottom=0.25)
plt.title('Square Wave')
plt.xlabel('Item Number')
plt.ylabel('Voltage')
plt.show()
