from heapq import *

def dijkstra(v, vn, E):
    D = [float('inf')] * (vn + 1)
    D[v] = 0
    vis = {v}
    if v not in E:
        return D
    for e in E[v]:
        u, c = e[0], e[1]
        D[u] = c
    heap = [(D[i], i) for i in range(1, vn + 1) if i != v]
    heapify(heap)
    
    while True:
        min_e = heappop(heap)
        D[min_e[1]] = min_e[0]
        vis.add(min_e[1])
        if len(heap) == 0:
            break
        if min_e[1] not in E:
            continue
        for e in E[min_e[1]]:
            u, c = e[0], e[1]
            if u in vis:
                continue
            if (D[u], u) in heap:
                if D[u] > min_e[0] + c:
                    heap.pop(heap.index((D[u], u)))
                    D[u] = min_e[0] + c
                    heappush(heap, (D[u], u))
            else:
                heappush(heap, (min_e[0] + c, u))
    return D
