def spiralOrder(matrix):
    l = []
    
    def dfs(matrix,i,j):
        if (i<0 or i>len(matrix)-1 or j<0 or j>len(matrix[0])-1 or matrix[i][j] == 'X'):
            return 
        l.append(matrix[i][j])
        matrix[i][j] = 'X'
        dfs(matrix,i,j+1)
        dfs(matrix,i+1,j)
        dfs(matrix,i,j-1)
        dfs(matrix,i-1,j)
    
    dfs(matrix,0,0)
        
    return l

l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
ans = (spiralOrder(l))
print(ans)