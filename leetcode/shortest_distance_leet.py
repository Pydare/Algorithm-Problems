from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_distance = float('inf') 
        total_ones = 0
        
        # count the total number of ones in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_ones += 1
        
        # loop through all empty lands and find the total diatance to other buildings
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    temp = self.building_distance(i, j, grid, total_ones)
                    min_distance = min(min_distance, temp)
                    
                    
        return -1 if min_distance == 0 or min_distance == float('inf') else min_distance
    
    def building_distance(self, i, j, grid, total_ones):
        seen = set((i,j))
        m, n = len(grid), len(grid[0])
        total = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up
        q = deque([((i,j), 0)])
        
        ones = 0
        while q:
            (i,j), d = q.popleft()
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and (x,y) not in seen:
                    seen.add((x,y))
                    if grid[x][y] == 1:
                        ones += 1
                        total += (d+1)
                    elif grid[x][y] == 2:
                        continue
                    else:
                        q.append(((x,y),d+1))
                        
        if ones != total_ones:
            return float('inf')
                        
        return total
                    
