import numpy as np
import matplotlib.pyplot as plt
filename = 'D:\magic04.txt'
a = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = np.mean(a, axis=0)
c1 = np.mat(a[:, 0])
c2 = np.mat(a[:, 1])
c1 = c1.T
c2 = c2.T
x = np.arange(0, 350)
y = x
plt.scatter(c1.tolist(), c2.tolist(), c=('b', 'r'))
plt.show()
