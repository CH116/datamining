import numpy as np
filename = 'D:\sjwj\iris.txt'
a = []
a = np.loadtxt(filename, comments='"', delimiter=',', usecols=(0, 1, 2, 3))
q = [[0 for x in range(10)] for y in range(a.shape[0])]
for k in range(0, a.shape[0]):
    p = 0
    for i in range(0, 4):
        for j in range(i, 4):
            if i == j:
                q[k][p] = (a[k][i])**2
            else:
                q[k][p] = np.sqrt(2) * a[k][i] * a[k][j]
            p = p + 1
n = np.mat(q)
m = n * n.T
print(m)
