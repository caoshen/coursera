with open('knapsack1.txt', 'r') as f:
    data = f.read().split('\n')

ks = int(data[0].split()[0])
kn = int(data[0].split()[1])
data = data[1: -1]

f = [0] * (ks + 1)


for i in data:
    v, w = int(i.split()[0]), int(i.split()[1])
    for n in range(ks, 0, -1):
        if n >= w:
            f[n] = max(f[n], f[n - w] + v)

print f[ks]
