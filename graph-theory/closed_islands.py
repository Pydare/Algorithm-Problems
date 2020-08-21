
def count_closed_islands(matrix,n,m):

    visited = [[False for _ in range(m)] for _ in range(n)]

    #mark all elements that are reachable from edge
    for i in range(n):
        for j in range(m):
            #traverse corners
            if (i*j == 0 or i == n-1 or j == m-1) and matrix[i][j] == 1 and not visited[i][j]:
                dfs(matrix,visited,i,j,n,m)

    result = 0
    for i in range(n):
        for j in range(m):
            #if land is not visited then there will be one closed island
            if not visited[i][j] and matrix[i][j] == 1:
                result += 1

                #mark all lands associated with island visited
                dfs(matrix,visited,i,j,n,m)

    return result

def dfs(matrix,visited,x,y,n,m):
    if not(0 <= x < n) or not(0 <= y < m) or visited[x][y] or matrix[x][y] == 0:
        return
    visited[x][y] = True

    dfs(matrix,visited,x+1,y,n,m)
    dfs(matrix,visited,x,y+1,n,m)
    dfs(matrix,visited,x-1,y,n,m)
    dfs(matrix,visited,x,y-1,n,m)

matrix = [[ 0, 0, 0, 0, 0, 0, 0, 1 ], 
            [ 0, 1, 1, 1, 1, 0, 0, 1 ], 
            [ 0, 1, 0, 1, 0, 0, 0, 1 ], 
            [ 0, 1, 1, 1, 1, 0, 1, 0 ], 
            [ 0, 0, 0, 0, 0, 0, 0, 1 ]]
ans = count_closed_islands(matrix,5,8)
print(ans)