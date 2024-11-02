from math import exp
import numpy as np
import matplotlib.pyplot as plt
import scipy

T1, T2 = 600, 1500  # début et fin
a, b = 0, 1 - 1e-15  # début et fin
xlist = np.linspace(T1, T2, num=T2 - T1)
listDichSP = []  #Scipy
listDichHM = []  #Fait maison


## FONCTIONS
def f(x, T):
    return ((x**2 * (3 - x) / (1 - x)**3) - exp(
        (1.98e5 - 188 * T) / (8.314 * T)))


def Dichotomie(T):
    a, b = 0, 1 - 1e-15  # début et fin
    diff = -15  # Ordre de grandeur
    while (b - a) > 10**diff:
        m = (a + b) / 2
        if (f(a, T) * f(m, T) <= 0):
            b = m
        else:
            a = m

    a, b = round(a, 1 - diff), round(b, 1 - diff)
    return (a, b)


## DICHOTOMIES
# SCIPY
for i in xlist:

    def F(x):
        return (f(x, i))

    listDichSP.append(scipy.optimize.bisect(F, a, b))

plt.plot(xlist, listDichSP)
plt.figure(num=0, dpi=120)

# FAIT MAISON
for i in xlist:
    listDichHM.append(Dichotomie(i))

plt.plot(xlist, listDichHM)
plt.figure(num=0, dpi=120)

plt.show()
