from collections import deque, namedtuple

#BFS SOLUTION
def flip_color(x,y,A):
    coordinate = namedtuple('coordinate',('x','y'))
    color = A[x][y]
    q = deque([coordinate(x,y)])
    A[x][y] = 1 - A[x][y]

    while q:
        x,y = q.popleft()
        for d in (0,1),(0,-1),(1,0),(-1,0):
            next_x,next_y = x+d[0],y+d[1]
            if 0<=next_x<len(A) and 0<=next_y<len(A[next_x]) and A[next_x][next_y]==color:
                #flips color
                A[next_x][next_y] = 1 - A[next_x][next_y]
                q.append(coordinate(next_x,next_y))

#DFS SOLUTION
def flip_color_dfs(x,y,A):
    color = A[x][y]
    A[x][y] = 1 - A[x][y]
    for d in (0,1),(0,-1),(1,0),(-1,0):
        nx,ny = x+d[0], y+d[1]
        if 0<=nx<len(A) and 0<=ny<len(A[nx]) and A[nx][ny]==color:
            flip_color_dfs(nx,ny,A)


#VARIANT CHALLENGE
def thickest_black_region(x,y,A):
    max_region = float('-inf')
    count = 0

    for x in range(len(A)):
        for y in range(len(A[x])):  
            color = A[x][y]
            q = deque([(x,y)])      
            while q:
                x,y = q.popleft()
                count += 1
                for d in (0,1),(0,-1),(1,0),(-1,0):
                nx,ny = x+d[0],y+d[1]
                    if 0<=nx<len(A) and 0<=ny<len(A[nx]) and A[nx][ny]==color:
                        #flips color
                        A[nx][ny] = 1 - A[nx][ny]
                        q.append(coordinate(nx,ny)) 
            max_region = max(max_region,count)

    return max_region


#DEADLOCK PROBLEM
class GraphVertex:

    white, gray, black = range(3)

    def __init__(self):
        self.color = GraphVertex.white
        self.edges = []

    def is_deadlock(G):
        def has_cycle(cur):
            #visiting a gray vertex means a cycle
            if cur.color == GraphVertex.gray:
                return True
            cur.color = GraphVertex.gray
            #traverse the neighbor vertices
            if any(nxt.color != GraphVertex.black and has_cycle(nxt) for nxt in cur.edges):
                return True
            cur.color = GraphVertex.black
            return False

        return any(vertex.color == GraphVertex.white and has_cycle(vertex) for vertex in G)