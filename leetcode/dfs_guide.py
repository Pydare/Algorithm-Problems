def spiralOrder(matrix):
    
    m, n = len(matrix), len(matrix[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #[right,down,left,up]
    res = []
    def dfs(x, y, d):
        visited[x][y] = True
        res.append(matrix[x][y])
        dx, dy = directions[d]
        r, c = x + dx, y + dy
        if 0 <= r < m and 0 <= c < n and not visited[r][c]:
            dfs(r, c, d)
        else:
            d = (d + 1) % 4
            dx, dy = directions[d]
            r, c = x + dx, y + dy
            if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                dfs(r, c, d)
            
    if not matrix or not matrix[0]:
        return []

    
    dfs(0, 0, 0)
    return res