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


##########CONNECTED COMPONENTS FOR ADJACENCY MATRIX##############
def findCircleNum(M):
        
    n,m = len(M),len(M[0])
    count = 0
    visited = [0]*m
    
    def dfs(i):
        for j in range(m):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                dfs(j)
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            count += 1
            
    return count



    
    