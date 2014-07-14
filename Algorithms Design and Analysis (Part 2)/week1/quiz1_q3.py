myfile = open("edges.txt", "r")
edges = myfile.read().split('\n')
myfile.close()

edge = edges[0].split()
vn, en = int(edge[0]), int(edge[1])
int_max = 1e20
mat = [([int_max] * vn) for i in range(vn)]  
nei = [-1] * vn
c = [0] + [int_max] * (vn - 1)
weight = 0
X = set([0])
Y = set()

for e in edges[1: -1]:
	edge = e.split()
	u, v, cost = int(edge[0]), int(edge[1]), int(edge[2])
	Y.update([u - 1, v - 1])
	mat[u - 1][v - 1] = cost
	mat[v - 1][u - 1] = cost

Y.remove(0)
for i in range(1, vn):
	if mat[0][i] != int_max:
		nei[i] = 0
		c[i] = mat[0][i]

for j in range(1, vn):
	vi ,v = int_max, -1
	for i in Y:
		if vi > c[i]:
			vi = c[i]
			v = i
	weight += c[v]
	X.add(v)
	Y.remove(v)
	for w in Y:
		if mat[v][w] != int_max:
			if mat[v][w] < c[w]:
				c[w] = mat[v][w]
				nei[w] = v
	
print weight
	