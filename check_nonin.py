import time

import serial

from systole.recording import Oximeter
from systole.utils import heart_rate

import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial("/dev/ttyUSB0")  # Add your USB port here

# Open serial port, initialize and plot recording for Oximeter
oxi = Oximeter(serial=ser, sfreq=75).setup()
# oxi.waitBeat()
#oxi = oxi.read(duration=20)

# oxi.save("good_data")

print("saved")

data = np.load("good_data.npy")

fig, ax = plt.subplots(3)

ax[0].plot(data[0], label="pleth plot")
ax[1].plot(data[1], label="heart rate (4 beats average)")
ax[1].plot(data[2], label="extended heart rate (8 beats average)")
ax[2].plot(data[3], label="SpO2")

for i in range(3):
    ax[i].legend()
# The signal can be directly plotted using built-in functions.
# oxi.plot_recording()
plt.show()

#hr = hr[np.logical_not(np.isnan(hr))]
# print(hr.mean())
# oxi.reset()
