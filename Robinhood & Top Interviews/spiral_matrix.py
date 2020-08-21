def spiral_order(matrix):

    def dfs(x,y,d):
        visited[x][y] = True
        output.append(matrix[x][y])
        dx, dy = directions[d]
        r,c = x+dx, y+dy
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and not visited[r][c]:
            dfs(r,c,d)
        else:
            d = (d+1) % 4
            dx, dy = directions[d]
            r, c = x+dx, y+dy
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and not visited[r][c]:
                dfs(r,c,d)

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    output = []
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    dfs(0,0,0)
    return output
