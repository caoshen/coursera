from time import *

start = time()

with open("g1.txt", 'r') as f:
    data = f.read().split('\n')

vn = int(data[0].split()[0])
en = int(data[0].split()[1])
data = data[1: -1]

A = [[float("inf")] * vn for i in range(vn)]

for i in data:
    edge = i.split()
    u, v, c = int(edge[0]), int(edge[1]), int(edge[2])
    A[u - 1][v - 1] = c

for i in range(vn):
    A[i][i] = 0

for k in range(vn):
    for i in range(vn):
        for j in range(vn):
            A[i][j] = min(A[i][j], A[i][k] + A[k][j])

flag = False
for i in range(vn):
    if A[i][i] < 0:
        flag = True
        break;

ret = float('inf')
if not flag:
    for i in range(vn):
        for j in range(vn):
            if i != j:
                ret = min(ret, A[i][j])
if flag:
    print 'input graph G has a negative cycle.'
else:
    print ret

end = time()

print 'Time: ', end - start
