import numpy as np
filename = 'D:\sjwj\iris.txt'
a = []
a = np.loadtxt(filename, comments='"', delimiter=',', usecols=(0, 1, 2, 3))
K = [[0 for x in range(a.shape[0])] for y in range(a.shape[0])]
for i in range(0, a.shape[0]):
    for j in range(0, a.shape[0]):
        c = a[i][0]*a[j][0]+a[i][1]*a[j][1]+a[i][2]*a[j][2]+a[i][3]*a[j][3]
        K[i][j] = c ** 2
# 先中心化
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

# 后标准化
f = []
# 计算每行的模
for i in range(a.shape[0]):
    f.append(np.sqrt(sum(x * x for x in q[i])))
    q[i] = q[i]/f[i]
# 求两两点积
m = np.zeros((a.shape[0], a.shape[0]))
for i in range(a.shape[0]):
    for j in range(a.shape[0]):
        m[i][j] = np.dot(q[i], q[j])
print(m)

