import numpy as np
filename = 'D:\magic04.txt'
a = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = np.mean(a, axis=0)
d = []
g = []
k = 0
for i in range(0, 10):
    for j in range(i+1, 10):
        c1 = np.mat(a[:, i])
        c2 = np.mat(a[:, j])
        e = np.cov(c1, c2)
        g = e
        if g[0][1] == 1324.8641308721578:
            print("最大协方差为第", i, "列与第", j, "列的协方差,值为：", 1324.8641308721578)
        if g[0][1] == -924.4341029748743:
            print("最小协方差为第", i, "列与第", j, "列的协方差,值为：", -924.4341029748743)
#       print(g[0][1])
#       d.append(g[0][1])


# dma = max(d)
# print(d)
# print("协方差最大值为：", dma, "协方差最小值为：", dmi)

