from time import *

start = time()

with open('clustering_big.txt', 'r') as f:
    data = f.read().split('\n')

vn = int(data[0].split()[0])
bn = int(data[0].split()[1])
data = data[1: -1]
my_dict = {}

iv = 0
for i in data:
    node_bit = int(''.join(i.split()), 2)
    if node_bit in my_dict:
        my_dict[node_bit].append(iv)
    else:
        my_dict[node_bit] = [iv]
    iv += 1

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

def my_merge(my_list1, my_list2):
    for u in my_list1:
        for v in my_list2:
            if u != v:
                my_union(u, v)

def dis(b1, b2):
    b = b1 ^ b2
    ret = 0
    while b > 0:
        b &= (b - 1)
        ret += 1
    return ret
    
for i in my_dict:
    #for j in my_dict:
    #   if i <= j and dis(i, j) < 3:
    #       my_merge(my_dict[i], my_dict[j])
    my_merge(my_dict[i], my_dict[i])
    for b in range(bn):
        j = i ^ (1 << b)
        if j in my_dict:
            my_merge(my_dict[i], my_dict[j])
    for b1 in range(bn - 1):
        for b2 in range(b1 + 1, bn):
            j = i ^ (1 << b1) ^ (1 << b2)
            if j in my_dict:
                my_merge(my_dict[i], my_dict[j])

cnt = 0
for i in range(vn):
    if p[i] == i:
        cnt += 1

print cnt


end = time()

print 'Time: ', end - start
