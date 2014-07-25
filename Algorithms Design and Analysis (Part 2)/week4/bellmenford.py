def bellmenford(s, vn, E):
    A = [[float('inf')] * (vn + 1) for i in range(vn + 1)]
    A[0][s] = 0
    i = 0
    for i in range(1, vn + 1):
        flag = True
        for v in E:
            A[i][v] = A[i - 1][v]
            for e in E[v]:
                u, c = e[0], e[1]
                A[i][v] = min(A[i][v], A[i - 1][u] + c)        
            if A[i][v] != A[i - 1][v]:
                flag = False                      
        if flag:
            break

    noNC = True
    for v in range(vn + 1):
        if A[i][v] != A[i - 1][v]:
            print 'input graph G has a negative cycle.'
            noNC = False
            break;
    if noNC:
        print 'no negative cycle.'
    return noNC, A[i]
