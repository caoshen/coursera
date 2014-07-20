with open('clustering1.txt', 'r') as f:
    data = f.read().split('\n')

vn = int(data[0])
data = data[1: -1]
edge_list = []

for i in data:
    edge = i.split()
    u, v, w = int(edge[0]), int(edge[1]), int(edge[2])
    edge_list.append((u - 1, v - 1, w))

def comp(edge1, edge2):
    return cmp(edge1[2], edge2[2])

edge_list.sort(comp)

p = [x for x in range(vn)]

def my_find(x):
    if x == p[x]:
        return x
    else:
        p[x] = my_find(p[x])
        return p[x]
    
def my_union(x, y):
    u, v = my_find(x), my_find(y)
    if u != v:
        p[u] = v
        return True
    else:
        return False

cnt = 0
for i in edge_list:
    u, v = i[0], i[1]
    if my_union(u, v) == True:
        del i
        cnt += 1
    if cnt == vn - 4:
        break

spacing = 0
for i in edge_list:
    u, v, w = i[0], i[1], i[2]
    if my_union(u, v) == True:
        spacing = w
        break

print spacing


