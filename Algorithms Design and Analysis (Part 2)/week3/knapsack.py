with open('knapsack1.txt', 'r') as f:
    data = f.read().split('\n')

ks = int(data[0].split()[0])
kn = int(data[0].split()[1])
data = data[1: -1]

f = [[0] * (ks + 1) for x in range(kn + 1)]


for i in data:
    v, w = int(i.split()[0]), int(i.split()[1])
    m = data.index(i) + 1
    for n in range(1, ks + 1):
        f[m][n] = f[m - 1][n]
        if n >= w:
            f[m][n] = max(f[m][n], f[m - 1][n - w] + v)

print f[kn][ks]
