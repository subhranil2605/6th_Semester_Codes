import numpy as np
from scipy.constants import pi, c, k, h
import matplotlib.pyplot as plt


def planck(lamb, T):
    lamb = np.array(lamb)
    return ((8*pi*h*c)/(np.power(lamb, 5)))/(np.exp((h*c)/(lamb*k*T)) - 1)


def rayleighJeans(lamb, T):
    lamb = np.array(lamb)
    return (8*pi*k*T)/(np.power(lamb, 4))


temps = [3e3, 4e3, 5e3]
w_ln = np.linspace(1e-8, 5e-6, 1000)
ps = [planck(w_ln, t) for t in temps]
rs = [rayleighJeans(w_ln, t) for t in temps]

[plt.plot(w_ln, p, label=f"Plank, T={temps[i]}K") for i, p in enumerate(ps)]
[plt.plot(w_ln, r, label=f"Rayleigh, T={temps[i]}K") for i, r in enumerate(rs)]

plt.ylim([0, 1000000])
plt.title("Planck's and Rayleigh radiation")
plt.xlabel('Wavelength (${\lambda}$)')
plt.ylabel('Energy density')
plt.legend(loc='upper right')
plt.show()
