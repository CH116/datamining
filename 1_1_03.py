import numpy as np
filename = 'D:\magic04.txt'
a = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = np.mean(a, axis=0)
c = np.mat(a[0])
z = (c - b).T*(c - b)
for i in range(1, a.shape[0]):
    c = np.mat(a[i])
    z = z + (c - b).T*(c - b)
print(z/a.shape[0])
