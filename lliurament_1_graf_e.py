import matplotlib.pyplot as plt
import numpy as np

k = 1
l = 1
T = 1
L = 1
N = 100
x = np.linspace(0,L,N)

def f(x):
    y = k*T/2*l * np.log((L+x)/(L-x))

    return y

plt.plot(x,f(x))
plt.show()