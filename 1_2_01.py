import numpy as np
filename = 'D:\sjwj\iris.txt'
a = []
a = np.loadtxt(filename, comments='"', delimiter=',', usecols=(0, 1, 2, 3))
K = [[0 for x in range(a.shape[0])] for y in range(a.shape[0])]
for i in range(0, a.shape[0]):
    for j in range(0, a.shape[0]):
        c = a[i][0]*a[j][0]+a[i][1]*a[j][1]+a[i][2]*a[j][2]+a[i][3]*a[j][3]
        K[i][j] = c ** 2
print(K)
