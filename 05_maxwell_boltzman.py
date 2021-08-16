import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k, e


def distribution(E, T, a):
    E = np.array(E)
    mu = 0 
    return 1/(np.exp(((E-mu)*e)/(k*T))+a)


temps = [1e3, 1.1e3]
es = [-0.5, 0.8]
energy = np.linspace(es[0], es[1], 100)
f_mbs = [distribution(energy, t, 0) for t in temps]
[plt.plot(energy, f, label=f'MB, T={temps[i]}') for i, f in enumerate(f_mbs)]
plt.xlabel('Energy (ev)')
plt.ylabel('f(E)')
plt.title("Maxwell-Boltzmann distribution")
plt.legend(loc='upper right')  
plt.show()
