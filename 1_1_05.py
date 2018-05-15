import numpy as np
import matplotlib.pyplot as plt
import math
filename = 'D:\magic04.txt'
a = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
c1 = np.mat(a[:, 0])
s = np.mean(c1.T, axis=0)
u = []
u = s.getA()
u = u[0][0]
d = np.var(c1, axis=1)
bzc = math.sqrt(d)
print(u, "  ", bzc)
x = np.linspace(u - 3*bzc, u + 3*bzc, 50)
y = np.exp(-(x - u) ** 2 / (2 * bzc ** 2))/(math.sqrt(2*math.pi)*bzc)
plt.plot(x, y, "r-", linewidth=2)
plt.grid(True)
plt.show()
