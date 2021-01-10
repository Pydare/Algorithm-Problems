class Solution:
    def numIslands(self, grid):
        if len(grid) == 0: return 0
        
        rows, cols = len(grid), len(grid[0])
        self.count = sum(grid[i][j] == "1" for i in range(rows) for j in range(cols))
        parent = list(range(rows * cols))
        rank = [0] * (rows*cols)
        
        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
        
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot: return
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
                rank[yroot] += rank[xroot]
            else:
                parent[yroot] = xroot
                rank[xroot] += rank[yroot]
            self.count -= 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    continue
                index = i*cols + j
                if j < cols-1 and grid[i][j+1] == "1":
                    union(index, index+1)
                if i < rows-1 and grid[i+1][j] == "1":
                    union(index, index+cols)
                    
        return self.count
    
    ######### NUM OF ISLANDS 2 ##############
    def numIslands2(self, m: int, n: int, positions):
        
        parent = list(range(m * n))
        rank = [0] * (m * n)
        island = [[0 for _ in range(n)] for _ in range(m)]
        self.count, res = 0, []
        
        if not positions:
            return res
        
        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
            
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
                rank[px] += rank[py]
            else:
                parent[py] = px
                rank[py] += rank[px]
            self.count -= 1
        
        seen = set() # for the purpose of self cycle
        for i, j in positions:
            if (i, j) in seen: # detecting self cycles
                res.append(self.count)
                continue
            seen.add((i, j))
            island[i][j] = 1
            self.count += 1
            idx = i*n + j   # row number * no. of columns + col number
            for dx, dy in (1,0), (0,1), (-1,0), (0,-1):
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and island[x][y] == 1:
                    idx2 = x*n + y
                    union(idx, idx2)
            res.append(self.count)
                    
        return res