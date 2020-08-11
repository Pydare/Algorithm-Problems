"""
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
"""
from collections import defaultdict
def valid_tree(edges,n):
    if len(edges) != n - 1: return False
    
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    parent = {0: -1}
    stack = [0]
    
    while stack:
        node = stack.pop()
        for neighbour in adj_list[node]:
            if neighbour == parent[node]: #this handles the undirected graph cycle issue
                continue
            if neighbour in parent:
                return False
            parent[neighbour] = node
            stack.append(neighbour)
    
    return len(parent) == n

ans = valid_tree([[0,1], [0,2], [0,3], [1,4]],5)
print(ans)
