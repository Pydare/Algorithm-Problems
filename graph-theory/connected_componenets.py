edges = [[0, 1], [1, 2], [3, 4]]


def count_components(n,edges):

    def dfs(node,adj_list,visited): #node is index, g is adj_list and visited in map
        if visited[node]:
            return
        visited[node] = 1

        for neighbor in adj_list[node]:
            dfs(neighbor,adj_list,visited)

    visited = [0] * n
    adj_list = [[] for _ in range(n)]
    for x,y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)

    ret = 0
    for i in range(n):
        if not visited[i]:
            dfs(i,adj_list,visited)
            ret += 1

    return ret



    
    