import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from cmath import phase

def results(freq, mag, phase, title, xlab, ylab):
    plt.title(title, size=18)
    plt.xlabel(xlab, size=18)
    plt.ylabel(ylab, size=18)
    plt.grid(1)
    plt.xscale('log')
    plt.plot(freq, mag, 'r')
    plt.show()
    return

freq = np.logspace(0, 9, 500)
w_freq = freq * 2 * np.pi


fc = 56.8 * 10**3.0
wc = fc * 2 * np.pi
Gain = float(1.77827941)

def LP(Gain, Q, fn):
    wnc = float(fn * wc)
    mag = Gain / (1.0 - (w_freq / wnc) ** 2.0 + (1j * w_freq / wnc) / Q)
    return mag


mag_8_cp = LP(Gain, 0.577, 1.274)*LP(Gain, 0.577, 1.274)*LP(Gain, 0.577, 1.274)*LP(Gain, 0.577, 1.274)
mag_8_ca = LP(Gain, 0.506, 1.784)*LP(Gain, 0.560, 1.838)*LP(Gain, 0.711, 1.958)*LP(Gain, 1.226, 2.196)

ph_1 = sp.angle(mag_8_cp)
ph_2 = sp.angle(mag_8_ca)

mag_8_ca = 20 * np.log10(np.abs(mag_8_ca))
mag_8_cp = 20 * np.log10(np.abs(mag_8_cp))

#mag_2 = LP(2, Q)
#mag_2 = 20 * np.log10(np.abs(mag_2))

#results(freq, mag, phase, "Test", "Hz", "dB")

plt.title("Phase of transfer Function (degrees) of 8th order Low Pass Filters against Frequency (Hz)", size=18)
plt.xlabel("Frequency (Hz)", size=18)
plt.ylabel("|H(f)| (dB)", size=18)
plt.grid(1)
plt.xscale('log')
plt.plot(freq, np.rad2deg(ph_2), 'r')
plt.plot(freq, np.rad2deg(ph_1), 'm')
#plt.axvline(x = 10**5, color = 'k', linestyle = '--')
#plt.axvline(x = 10**6, color = 'k', linestyle = '--')
#plt.axvline(x = fc, color = 'b', linestyle = '--')
#plt.axhline(y = -3, color = 'k', linestyle = '--')
#plt.axhline(y = mag_8_ca[0] - 3, color = 'k', linestyle = '--')
plt.show()

#mag_8 = LP(2.0, 0.506)*LP(1.0, 0.56)*LP(1.0, 0.711)*LP(1.0, 1.226)
#ph_2 = sp.angle(mag_8)
#mag_8 = 20 * np.log10(np.abs(mag_8))

#mag_2 = LP(1, 0.506)
#mag_2 = 20 * np.log10(np.abs(mag_2))

#plt.plot(freq, mag_8, 'g')
#plt.plot(freq, mag_2, 'm')
#plt.show()

#plt.title("Phase of Transfer Function (degrees) of an order 8 Low Pass Filter against Frequency (Hz)", size=18)
#plt.xlabel("Frequency (Hz)", size=18)
#plt.ylabel("|H(f)| (dB)", size=18)
#plt.grid(1)
#plt.xscale('log')
#plt.plot(freq, ph_1, 'r')
#plt.plot(freq, ph_2, 'm')
#plt.show()
