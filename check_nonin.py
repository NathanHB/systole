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
oxi = oxi.read(duration=20)

spo2 = oxi.oxigen_levels
hr = oxi.heart_rate

print(f"hr: {hr}")
print(f"spo2: {spo2}")

fig, ax = plt.subplots(3)

ax[0].plot(hr)
ax[1].plot(spo2)
ax[2].plot(oxi.recording)

# The signal can be directly plotted using built-in functions.
# oxi.plot_recording()
plt.show()

#hr = hr[np.logical_not(np.isnan(hr))]
# print(hr.mean())
# oxi.reset()
