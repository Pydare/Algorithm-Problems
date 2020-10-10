from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.neighbors = [(0,-1),(-1,0),(0,1),(1,0)]

    def shortest_distance(self,grid):
        self.grid = grid
        self.initialize()
        for building in self.buildings:
            self.bfs(building)
        return self.best_location()

    def initialize(self):
        self.buildings, self.empty = set(), set()
        self.shortest_path_sum = defaultdict(int)
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 0:
                    self.empty.add((r,c))
                elif self.grid[r][c] == 1:
                    self.buildings.add((r,c))

    def bfs(self,start):
        q, visited = deque([(*start,0)]), set()
        shortest_paths = {k:float('inf') for k in self.empty}
        while q:
            r,c,dist = q.popleft()
            if self.grid[r][c] != 0 and dist > 0:
                continue
            if (r,c) in visited:
                continue
            if (r,c) in shortest_paths:
                shortest_paths[(r,c)] = dist
            visited.add((r,c))