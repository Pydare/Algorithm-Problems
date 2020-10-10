from collections import namedtuple
WHITE, BLACK = range(2)

coordinate = namedtuple('coordinate',('x','y'))

def search_maze(maze,s,e):
    #perform dfs to find a feasible path
    def maze_search_helper(curr):
        #check curr is within maze and is a white pixel
        if not (0<=curr.x<len(maze) and 0<+curr.y<len(maze[curr.x]) and maze[curr.x][curr.y]==WHITE):
             return False
        path.append(curr)
        maze[curr.x][curr.y] = BLACK
        if curr == e:
            return True
        if any(
            map(maze_search_helper, (coordinate(curr.x-1,curr.y),
            coordinate(curr.x+1,curr.y),coordinate(curr.x,curr.y-1),
            coordinate(curr.x,curr.y+1)
            ))
        ):
        return True

        #cannot find a path, remove the entry added in path.append(curr)
        del path[-1]
        return False

    path = []
    if not maze_search_helper(s):
        return [] #no path between s and e
    return path