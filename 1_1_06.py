import numpy as np
filename = 'D:\magic04.txt'
a = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = np.mean(a, axis=0)
d = []
for i in range(0, 10):
    c = np.mat(a[:, i])
    e = np.var(c)
    d.append(e)
dma = max(d)
dmi = min(d)
print("方差MAX为：", dma, "方差MIN为：", dmi)
