"""

"""

def leads_to_destination(n, edges, source, destination):
    adj_list = [[] for _ in range(n)]
    for x,y in edges:
        adj_list[x].append(y)
        #adj_list[y].append(x)

    seen = set()
    def dfs(source, destination, node):
        if adj_list[node] == [] and node != destination:
            return False
        if node == destination and len(seen) == n:
            return True
        if adj_list[node] == [] and node == destination:
            return True

        seen.add(node)
        for neighbor in adj_list[node]:
            if neighbor in seen:
                continue
            res = dfs(source, destination, neighbor)
            if not res:
                return False
            else:
                return True

    return dfs(source, destination, 0)

ans = leads_to_destination(4, [[0,1],[1,1],[1,2]], 0, 2)
print(ans)


from collections import defaultdict

#could  be used for cycle detection
def correction(n, edges, source, destination):
    g = defaultdict(set)
    visited = defaultdict(int)

    for x,y in edges:
        g[x].add(y)

    def dfs(node):
        if visited[node] == 1:
            return True
        elif visited[node] == -1:
            return False
        elif len(g[node]) == 0:
            return node == destination
        else:
            visited[node] = -1
            for child in g[node]:
                if not dfs(child):
                    return False
            visited[node] = 1
            return True

    return dfs(source)