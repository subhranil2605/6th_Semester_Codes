import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k, e


def distribution(E, T, a):
    E = np.array(E)
    mu = 0
    return 1/(np.exp(((E-mu)*e)/(k*T))+a)


temps = [0, 500, 1000, 2000]
es = [-1, 1]
energy = np.linspace(es[0], es[1], 100)
f_fds = [distribution(energy, t, 1) for t in temps]
[plt.plot(energy, f, label=f"FD, T={temps[i]}K") for i, f in enumerate(f_fds)]
plt.xlabel('Energy (ev)')
plt.ylabel('f(E)')
plt.title("Fermi-Dirac distribution")
plt.legend(loc='upper right')
plt.show()
