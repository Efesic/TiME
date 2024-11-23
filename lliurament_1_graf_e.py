import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams.update({'font.size': 16.5})

N = 100
x = np.linspace(-1,1,N)

def f(x):

    y = np.log((1+x)/(1-x))

    return y

plt.figure(figsize=(8,6))
plt.plot(x,f(x), color = 'firebrick')
plt.xlabel('$R/L$')
plt.ylabel('$\\tau$')
plt.minorticks_on()
plt.tick_params(which= 'major', direction='in',top = True,right =True,size = 10)
plt.tick_params(which= 'minor', direction='in',top = True,right =True,size = 5)
plt.grid(linestyle='--')
plt.show()