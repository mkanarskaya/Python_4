import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sc
A1 = 10
w1 = 15*2*math.pi
A2 = 10
w2 = 5*2*math.pi
A3 = 10
w3 = 10*2*math.pi
Anoise = 10
T1 = -10
T2 = 10
SIZE_TIME = 1000
Time = np.linspace(T1, T2, SIZE_TIME)


sign1 = np.array([A1*math.sin(w1*t) for t in Time])
sign2 = np.array([A2*math.sin(w2*t) for t in Time])
sign3 = np.array([A2*math.sin(w2*t) for t in Time])
noise = 2*Anoise*(np.random.random(SIZE_TIME)-0.5)
pure_sign = sign1 + sign2 + sign3
dirty_sign = pure_sign + noise
plt.plot(Time, dirty_sign)
plt.plot(Time, pure_sign)
plt.xlabel(u'Время, c')
plt.ylabel(u'Напряжение, мВ')
plt.grid(True)
plt.savefig('dirty_signal_1.png')
plt.show()

spectrum = sc.rfft(dirty_sign)
plt.plot(sc.rfftfreq(len(Time), d = (T2-T1)/SIZE_TIME), np.abs(spectrum) / len(Time))
plt.xlabel(u'Частота, Гц')
plt.ylabel(u'Напряжение, мВ')
plt.grid(True)
plt.savefig('Spectrum1.png')
plt.show()

for i in range(len(spectrum)):
    if np.abs(spectrum[i])*5 > max(np.abs(spectrum)):
        spectrum[i] = spectrum[i]
    else:
        spectrum[i] = 0
plt.plot(sc.rfftfreq(len(Time), d = (T2-T1)/SIZE_TIME), np.abs(spectrum) / len(Time))
plt.xlabel(u'Частота, Гц')
plt.ylabel(u'Напряжение, мВ')
plt.grid(True)
plt.savefig('Spectrum2.png')
plt.show()
new_sign = sc.irfft(spectrum)
plt.plot(Time[:len(Time)//10], new_sign[:len(Time)//10], label = 'new signal')
plt.plot(Time[:len(Time)//10], dirty_sign[:len(Time)//10], label = 'new signal')
plt.plot(Time[:len(Time)//10], pure_sign[:len(Time)//10], label = 'new signal')
plt.legend()
plt.xlabel(u'Время, c')
plt.ylabel(u'Напряжение, мВ')
plt.grid(True)
plt.savefig('dirty_signal_2.png')
plt.show()
