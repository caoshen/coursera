from time import *

start = time()
with open('knapsack_big.txt', 'r') as f:
    data = f.read().split('\n')

ks = int(data[0].split()[0])
kn = int(data[0].split()[1])
data = data[1: -1]

pre = [[0, 0]]
cur = []

for i in data:
    v, w = int(i.split()[0]), int(i.split()[1])
    pre_w = [[x[0] + w, x[1] + v] for x in pre if x[0] + w <= ks]
    cur = [[0, 0]]
    j, k = 0, 0
    while j < len(pre) and k < len(pre_w):
        if pre[j][0] < pre_w[k][0]:
            if cur[-1][1] < pre[j][1]:
                cur.append(pre[j])
            j += 1
        else:
            if cur[-1][1] < pre_w[k][1]:
                cur.append(pre_w[k])
            k += 1
    while j < len(pre):
        if cur[-1][1] < pre[j][1]:
            cur.append(pre[j])
        j += 1
    while k < len(pre_w):
        if cur[-1][1] < pre_w[k][1]:
            cur.append(pre_w[k])
        k += 1
    pre = cur

print cur[-1][1]

end = time()

print "Time: ", end - start
