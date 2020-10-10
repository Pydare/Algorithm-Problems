def search_maze(maze,s,e):
    white, black = range(2)
    m,n = len(maze),len(maze[0])
    path = []

    def helper(i,j):
        #check curr is within maze and is white
        if not (0<=i<m and 0<=j<n and maze[i][j]==white):
            return False
        path.append((i,j))
        maze[i][j] = black
        if (i,j) == e:
            return True
        if helper(i-1,j) or helper(i+1,j) or helper(i,j-1) or helper(i,j+1):
            return True
        
        #cannot find a path
        path.pop()
        return False

    return path