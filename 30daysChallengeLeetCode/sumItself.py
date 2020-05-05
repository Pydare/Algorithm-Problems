from collections import namedtuple

WHITE, BLACK = range(2)

coordinate = namedtuple('coordinate',('x','y'))

def search_maze(maze,s,e):
    #perform dfs to find a feasible path
    def search_maze_helper(cur):
        #checks cur is within maze and is a white pixel
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE:
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True
        
        if any(map(search_maze_helper,(coordinate(cur.x-1,cur.y),coordinate(cur.x+1,cur.y),
                coordinate(cur.x,cur.y-1), coordinate(cur.x,cur.y+1)))):
            return True
        #cannot find a path, remove the entry added in path.append(cur)
        del path[-1]
        return False
    path = []
    if not search_maze_helper(s):
        return [] #no path between s & e.
    return path
