from collections import defaultdict

def all_critical_connections(n, edges):
    res = []

    i = 0
    while i < n:
        temp_edges = edges[:i] + edges[i+1:]
        adj_list = defaultdict(list)
        
        for x, y in temp_edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        if not is_connected(adj_list, n):
            res.append(edges[i])

        i += 1

    return res


def is_connected(adj_list, n):
    seen = set()
    count = 0

    def dfs(i):
        seen.add(i)
        for nei in adj_list[i]:
            if nei not in seen:
                dfs(nei)

    for i in range(n):
        if i not in seen:
            dfs(i)
            count += 1

    return count == 1

ans = all_critical_connections(4, [[0,1],[1,2],[2,0],[1,3]])
print(ans)


###########LEETCODE O(V+E) ##############
from collections import defaultdict
class Solution:
    def criticalConnections(self, n, connections):
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