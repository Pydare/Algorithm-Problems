def cherryPickup(grid):
    total_cherries = 0
    n = len(grid) # no. of rows
    m = len(grid[0]) # no. of columns
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                total_cherries = dfs_down(grid,i,j,0)
                break
    return total_cherries
                
def dfs_down(grid,i,j,cherry):
    if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j] == -1:
        return

    if i == len(grid)-1 and j == len(grid[0])-1:
        returning = dfs_up(grid,i,j,0)
        
    if grid[i][j] == 1:
        grid[i][j] = 0
        cherry += 1
    dfs_down(grid,i+1,j,cherry)   
    dfs_down(grid,i,j+1,cherry)
    
    return cherry + returning

def dfs_up(grid,i,j,ch): #keep checking if there's a 1, if not return 0
    if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]==-1:
        return
    if grid[i][j] == 1:
        grid[i][j] = 0
        ch += 1
        
    if sum(grid[i]) > 0: # sum of row > 0, ie, there's at a least 1
        dfs_up(grid,i,j-1,ch)
    col_len = 0
    for k in range(0,j):
        col_len += grid[i][k]
    if col_len > 0: # sum of column > 0, ie, at least there's a cherry
        dfs_up(grid,-1,j,ch)
    else:
        dfs_up(grid,i,j-1,ch)
        dfs_up(grid,-1,j,ch)
    
    return ch

grid =[[0, 1, -1],[1, 0, -1],[1, 1,  1]]  
ans =  cherryPickup(grid)
print(ans)
    
    
    