import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
angles = np.arange(0, 3*np.pi, 0.1) # siapkan nilai utk sumbu x
sindata = np.sin(angles) # siapkan nilai utk sumbu y
fig, ax = plt.subplots()
line, = ax.plot([], [], color='g')
ax.axis([0, 3 * np.pi, -1, 1]) # atur rentang nilai sumbu x dan y
plt.title('Animasi gelombang sinus') # judul grafik
plt.xlabel('Sudut (radian)') # judul sumbu x
plt.ylabel('Sinus') # judul sumbu y
plt.grid(True, which='both') # tampilkan grid/kotak-kotak
def update(num, line):
    line.set_data(angles[:num], sindata[:num])
    return line,
ani = animation.FuncAnimation(fig, update, fargs=[line],interval=10)
ani.save('anim/sine.gif', writer='imagemagick', fps=30)
