import math

# Prims Algorithim for Minimum Spanning Tree(MST): O(n^2)

def prim2(G, r):
    n = len(G)
    p = [(None, math.inf)] * n  
    p[r] = (None, 0) 
    min_span_tree = []

    while True:
        min_proximity = math.inf 
        min_vertex = None 
        for k in range(n): 
            if not min_span_tree and G[r][k] < p[k][1]:
                p[k] = (r, G[r][k])

            if p[k][1] < min_proximity and p[k][0] is not None and k not in [x[1] for x in min_span_tree]:
                min_proximity = p[k][1]
                min_vertex = k
        if min_vertex is None:
            break
        u = p[min_vertex][0]
        min_span_tree.append((u, min_vertex))

        for v in range(n):
            if G[min_vertex][v] < p[v][1]:
                p[v] = (min_vertex, G[min_vertex][v])

    return min_span_tree

# Test:

g1 = [
[ 0, 4, 0, 0, 0, 0, 0, 8, 0],
[ 4, 0, 8, 0, 0, 0, 0, 11, 0],
[ 0, 8, 0, 7, 0, 4, 0, 0, 2],
[ 0, 0, 7, 0, 9, 14, 0, 0, 0],
[ 0, 0, 0, 9, 0, 10, 0, 0, 0],
[ 0, 0, 4, 14, 10, 0, 2, 0, 0],
[ 0, 0, 0, 0, 0, 2, 0, 1, 6],
[ 8, 11, 0, 0, 0, 0, 1, 0, 7],
[ 0, 0, 2, 0, 0, 0, 6, 7, 0] ]
print(prim2(g1, 0))

g2 = [ [ 0, 8, 5, 9, 6, 3],
[ 8, 0, 2, 2, 5, 2],
[ 5, 2, 0, 3, 1, 7],
[ 9, 2, 3, 0, 1, 9],
[ 6, 5, 1, 1, 0, 9],
[ 3, 2, 7, 9, 9, 0] ]
print(prim2(g2, 0))


# Prims algorithims for second MST 

def secondMST(G):
    n = len(G)
    min_span_tree = prim2(G, 0)
    second_weight = float('inf')
    second_tree = []
    MST_weight = sum(G[u][v] for u, v in min_span_tree)
    
    for u, v in min_span_tree:
        original_weight = G[u][v]
        G[u][v] = math.inf  
        G[v][u] = math.inf
        new_span_tree = prim2(G, 0)
        new_span_tree_weight = sum(G[u][v] for u, v in new_span_tree if G[u][v] != math.inf)
        G[u][v] = original_weight
        G[v][u] = original_weight
        if new_span_tree_weight < second_weight:
            second_weight = new_span_tree_weight
            second_tree = new_span_tree

    return second_tree

# Test:

g1 = [
[ 0, 4, 0, 0, 0, 0, 0, 8, 0],
[ 4, 0, 8, 0, 0, 0, 0, 11, 0],
[ 0, 8, 0, 7, 0, 4, 0, 0, 2],
[ 0, 0, 7, 0, 9, 14, 0, 0, 0],
[ 0, 0, 0, 9, 0, 10, 0, 0, 0],
[ 0, 0, 4, 14, 10, 0, 2, 0, 0],
[ 0, 0, 0, 0, 0, 2, 0, 1, 6],
[ 8, 11, 0, 0, 0, 0, 1, 0, 7],
[ 0, 0, 2, 0, 0, 0, 6, 7, 0]]
print(secondMST(g1))

g2 = [
[ 0, 8, 5, 9, 6, 3],
[ 8, 0, 2, 2, 5, 2],
[ 5, 2, 0, 3, 1, 7],
[ 9, 2, 3, 0, 1, 9],
[ 6, 5, 1, 1, 0, 9],
[ 3, 2, 7, 9, 9, 0] ]
print(secondMST(g2))