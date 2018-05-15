import numpy as np
filename = 'D:\magic04.txt'
a = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = np.mean(a, axis=0)
c = a - 1*b.T
z = np.mat(c)
n = z.shape[0]
answer = (z.T*z)*(1/n)
print(answer)
