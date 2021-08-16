import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k, e


def distribution(E, T, a):
    E = np.array(E)
    mu = 0
    return 1/(np.exp(((E-mu)*e)/(k*T))+a)


temps = [1e3, 2e3]
es = [0.0, 0.8]
energy = np.linspace(es[0], es[1], 100)
f_bes = [distribution(energy, t, -1) for t in temps]
[plt.plot(energy, f, label=f'BE, T={temps[i]}K') for i, f in enumerate(f_bes)]
plt.xlim([0, es[1]])
plt.ylim([0, 20])
plt.xlabel('Energy (ev)')
plt.ylabel('f(E)')
plt.title("Bose-Einstein distribution")
plt.legend(loc='upper right')
plt.show()
