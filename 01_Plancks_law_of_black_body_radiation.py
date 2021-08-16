import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi, c, k, h


def Planck(lamb, T):
    lamb = np.array(lamb)
    return ((8*pi*h*c)/(np.power(lamb, 5)))/(np.exp((h*c)/(lamb*k*T)) - 1)


temps = [3e3, 4e3, 5e3]
w_ln = np.linspace(1e-8, 5e-6, 1000)
[plt.plot(w_ln, Planck(w_ln, i), label=f'T={i}K') for i in temps]
plt.xlabel('Wavelength ($\lambda$)')
plt.ylabel('Energy density')
plt.title("Plot of Plank's radiation formula")
plt.legend(loc='upper right')
plt.show()
