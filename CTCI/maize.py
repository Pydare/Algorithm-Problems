def search_maize(maze,s,e):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            pass

def dfs(board,i,j,e):
    if i<0 or i>len(board)-1 or j<0 or j>len(board[i]-1) or board[i][j] == 0:
        return False
    board[i][j] = 0
    dfs(board,i+1,j)
    dfs(board,i-1,j)
    dfs(board,i,j+1)
    dfs(board,i,j-1)
    if board[i][j] == e:
        return True