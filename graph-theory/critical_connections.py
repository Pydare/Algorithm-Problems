"""
In DFS tree, a vertex u is articulation point if one of the following two conditions is true.
1) u is root of DFS tree and it has at least two children.
2) u is not root of DFS tree and it has a child v such that no vertex in subtree rooted with v has a back edge to one of the ancestors (in DFS tree) of u.
"""
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        
        pre = [-1 for i in range(n)]
        low = [-1 for i in range(n)]
        order = 0    
        ans = []
        
        def dfs(par, cur, order):
            order += 1
            pre[cur] = order
            low[cur] = pre[cur]
            for w in graph[cur]:
                if (pre[w] == -1):
                    dfs(cur, w, order)
                    low[cur] = min(low[cur], low[w])
                    if (low[w] == pre[w]):
                        ans.append((cur, w))
                
                elif (w != par):
                    low[cur] = min(low[cur], pre[w])
        
        dfs(0, 0, 0) # this can be any random node, since from one node can reach any other node, dfs(1, 1, 0) will also work

        return ans