import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter
matplotlib.rcParams.update({'font.size': 20})

# Funció del valor esperat de R
def R(f,T):
    return np.tanh(f/T)

# Com varia segons la força
T_a = 100
plt.figure(figsize=(8,6))
f = np.linspace(1,1000,1000)
R_f = R(f,T_a)
plt.scatter(f,R_f,s=4,color='firebrick')
plt.xlabel('$\hat{f}$')
plt.ylabel('$\langle \hat{R} \\rangle$')
plt.minorticks_on()
plt.tick_params(which= 'major', direction='in',top = True,right =True,size = 10)
plt.tick_params(which= 'minor', direction='in',top = True,right =True,size = 5)
plt.grid(linestyle='--')
plt.tight_layout(pad=0.2)
plt.savefig('Lliurament_2/document_L2/plots/canvi_f.png',dpi=300)

# Com varia segons la temperatura
f_a = 100
plt.figure(figsize=(8,6))
T = np.linspace(1,3000,1000)
R_T = R(f_a,T)
plt.scatter(T,R_T,s=4,color='forestgreen')
plt.xlabel('$\hat{T}$')
plt.ylabel('$\langle \hat{R} \\rangle$')
plt.minorticks_on()
plt.tick_params(which= 'major', direction='in',top = True,right =True,size = 10)
plt.tick_params(which= 'minor', direction='in',top = True,right =True,size = 5)
plt.grid(linestyle='--')
plt.tight_layout(pad=0.2)
plt.savefig('Lliurament_2/document_L2/plots/canvi_T.png',dpi=300)

matplotlib.rcParams.update({'font.size': 13})
# Generació del gràfic 3D en diferents perspectives
angles_list = [45,135,225,315]
for i in angles_list:
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d') 
    x = np.linspace(100,1000,1000)
    y = np.linspace(100,1000,1000)
    X, Y = np.meshgrid(x,y)
    Z = R(X,Y)
    ax.view_init(elev=20, azim=i)
    ax.set_xlabel('$\hat{f}$ [J]')
    ax.set_ylabel('$\hat{T}$ [J]')
    ax.set_zlabel('$\langle \hat{R} \\rangle$ [m]')
    ax.plot_surface(X, Y, Z, cmap='coolwarm')
    plt.savefig(f'Lliurament_2/document_L2/plots/canvi_3D_{i}.png',dpi=300)

# Animació del gràfic 3D
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
x = np.linspace(100,1000,1000)
y = np.linspace(100,1000,1000)
X, Y = np.meshgrid(x,y)
Z = R(X,Y)
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')
ax.set_xlabel('$\hat{f}$ [J]')
ax.set_ylabel('$\hat{T}$ [J]')
ax.set_zlabel('$\langle \har{R} \\rangle$ [m]')
def update(angle):
    ax.view_init(elev=30, azim=angle)
    return [surf]
ani = FuncAnimation(fig, update, frames=range(0, 360, 1), interval=75, blit=True)
writer = PillowWriter(fps=30)  
ani.save("Lliurament_2/document_L2/plots/animacio.gif", writer=writer)



