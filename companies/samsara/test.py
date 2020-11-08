start = 65
grid = [["" for _ in range(6)] for _ in range(5)]

m,n = len(grid), len(grid[0])
for i in range(m):
    for j in range(n):
        grid[i][j] = chr(start)
        start += 1

print(grid)