def binaryMatrixShortestPath(grid):
    N = len(grid)
    if N == 0 or grid[0][0] != 0 or grid[N - 1][N - 1] != 0:
        return -1

    