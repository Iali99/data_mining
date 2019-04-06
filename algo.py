import math

# assuming G given as distance matrix, L given as nx3 matrix with columns as source, destination, traffic weight
dist_matr = np.zeros(n, n)
indx_dict = {}
traffic_matr = np.zeros(k, 3)
edges = []      # tuple of source and destination

n = dist_matr.shape[0]
m = len(edges)


def cost_edges(R):    # R is a set of edges
    cost = 0
    for items in R:
        cost += dist_matr[items[0], items[1]]
    return cost


l = {}   # dict: edge -> l

R = set()
lamda = math.inf

for edge in edges:
    l[edge] = dist_matr[edge[0], edge[1]]       # edge weight between source and destination

while B>0 and lamda>1:
    pmin = set()       # shortest path
    lamda_min = math.inf 
    for i in range(k):
        item = traffic_matr[i]
        pi = shortest_path(item[0], item[1], dist_matr, l)      # returns a set of edges
        if lamda_min > stretch_factor(R.union(pi), dist_matr, l):
            pmin = pi

    R1 = pmin - R

    C = cost_edges(R1)

    if C:
        return R
    R = R.union(R1)

    for edges in R1:
        l[edge] = 0
    B = B - C
    lamda = stretch_factor(R, dist_matr, l):

return R
