from time import *
from bellmenford import *
from dijkstra import *

start = time()

with open("g3.txt", 'r') as f:
    data = f.read().split('\n')

vn = int(data[0].split()[0])
en = int(data[0].split()[1])
data = data[1: -1]

E = {}
E2 = {}

# add new source 0
for i in range(1, vn + 1):
    E[i] = [[0, 0]]
    
for i in data:
    edge = i.split()
    u, v, c = int(edge[0]), int(edge[1]), int(edge[2])
    E[v].append([u, c])
    if u in E2:
        E2[u].append([v, c])
    else:
        E2[u] = [[v, c]]

# bellmen-ford, true if no negative cycle
# A is single source shortest path from source 0
noNC, A = bellmenford(0, vn + 1, E)
    
if noNC:
     
    # c'[u][v] = c[u][v] + A[u] - A[v]
    for u in E2:
        for e in E2[u]:
            e[1] += A[u] - A[e[0]]
            
    # all pair shortest distance
    D = [[0] * (vn + 1) for i in range(vn + 1)]

    # n dijkstra
    for n in range(1, vn + 1):
        D[n] = dijkstra(n, vn, E2)

    # D[u][v] = D[u][v] - A[u] + A[v]
    ret, x, y = float('inf'), -1, -1
    for u in range(1, vn + 1):
        for v in range(1, vn + 1):
            D[u][v] += - A[u] + A[v]
            if ret > D[u][v]:
                ret, x, y = D[u][v], u, v
            
    # shortest path in all pairs      
    print ret, 'from', x, 'to', y
                   
end = time()

print 'Time: ', end - start
