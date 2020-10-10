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

##connected components in an undirected graph ---> BEST GUY FOR THE JOB
from collections import defaultdict
def countComponents(n,edges):
        
    def dfs(node):
        seen.add(node)
        for nei in adj_list[node]:
            if nei not in seen:
                dfs(nei)
                
    adj_list = defaultdict(list)
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    seen = set()
    count = 0
    for node in range(n):
        if node not in seen:
            dfs(node)
            count += 1
    return count


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



    
    