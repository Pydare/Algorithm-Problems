
"""
[[1,1,1],
 [1,2,0],
 [1,0,1]]
"""

def flood_fills(image,sr,sc,new_color):

    R,C = len(image), len(image[0])
    color = image[sr][sc]
    if color == new_color:
        return image

    def dfs(r,c):
        if image[r][c] != color:
            return 
        else:
            image[r][c] = new_color
            if r >= 1:
                dfs(r-1,c) #go up if row is >= 1
            if r+1 < R:
                dfs(r+1,c) #go down if row+1 is < R
            if c >= 1:
                dfs(r,c-1) #go left if column >= 1
            if c+1 < C:
                dfs(r,c+1) #go right if column+1 < C

    dfs(sr,sc)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
ans = flood_fills(image,1,1,2)
print(ans)