import numpy as np
from matplotlib import pyplot as plt
from scipy.constants import k, e


def distribution(E: np.array, T, a):
    mu = 0
    return 1/(np.exp(((E-mu)*e)/(k*T)) + a)


temp = 1000
e_0 = 0
e_1 = -0.80
e_2 = 0.80
energy = np.linspace(e_1, e_2, 100)
energy_0 = np.linspace(e_0, e_2, 100)
f_mb = distribution(energy, temp, 0)
f_be = distribution(energy_0, temp, -1)
f_fd = distribution(energy, temp, 1)
plt.plot(energy, f_mb, label="MB, T=1000K")
plt.plot(energy_0, f_be, label="BE, T=1000K")
plt.plot(energy, f_fd, label="FD, T=1000K")
plt.ylim([0, 2])
plt.xlabel('Energy (ev)')
plt.ylabel('f(E)')
plt.title("MB, BE & FD distribution")
plt.legend(loc='upper right')
plt.show()
