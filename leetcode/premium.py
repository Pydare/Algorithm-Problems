class Solution:
    def hasPath(self,maze,start,destination):
        self.answer = False
        self.visited = [[False for k in range(len(maze[0]))] for j in range(len(maze))]
        self.dfs(maze,start,destination)
        return self.answer

    def next_move(self,point,maze):
        i,j = point[0],point[1]
        row = len(maze) -1
        col = len(maze[0]) - 1

        x,y = i,j
        #try right
        while (y+1 <= col and maze[y+1]==0):
            y += 1
        if not (self.visited[x][y]):
            return [x,y]

        #try left
        x,y = i,j
        while (y-1 <= col and maze[y-1]==0):
            y -= 1
        if not (self.visited[x][y]):
            return [x,y]

        #try up 
		x,y = i,j
        while (x-1 >= 0 and maze[x-1][y] == 0):
            x -= 1
        if not self.visited[x][y]:
            return [x,y]

        #try down
		x, y = i , j
		while(x + 1 <= row and maze[x + 1][y] == 0):
			x += 1
		if not(self.visited[x][y]):
			return [x, y]

		return None

    def dfs(self,maze,point,dest):
        if not point:
            return
        x = point[0]
        y = point[1]
        if point == dest:
            self.answer = True
        self.visited[x][y] = True
        while self.next_move(point,maze):
            self.dfs(maze,self.next_move(point,maze),dest)