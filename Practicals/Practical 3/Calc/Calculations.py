
import numpy as np

w = 2 * np.pi * 72.4 * 10**3
c = 1 / (1j * 4.8324E-07 * w)
l1 = 1j * w * 2.0000E-06
l2 = 1j * w * 8.0000E-06

ser = l1 + l2
par = (1 / c) + (1 / ser)
sum = 1 / par

print("Tank: \n"+str(sum))
