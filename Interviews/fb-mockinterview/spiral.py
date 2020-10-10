def spiral_order(matrix):
    m,n = len(matrix), len(matrix[0])
    seen = set()
    res = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i,j,d):
        seen.add((i,j))
        res.append(matrix[i][j])
        dx, dy = directions[d]
        x, y = i+dx, j+dy
        if 0<=x<m and 0<=y<n and (x,y) not in seen:
            dfs(x,y,d)
        else:
            d = (d+1)%4
            dx,dy = directions[d]
            x, y = i+dx, j+dy
            if 0<=x<m and 0<=y<n and (x,y) not in seen:
                dfs(x,y,d)