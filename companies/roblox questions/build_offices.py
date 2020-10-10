import itertools
from collections import deque

def build(height,width,n):
    arr = []
    for i in range(height):
        for j in range(width):
            arr.append((i,j,0))

    ans = float("inf")
    for points in itertools.combinations(arr,n):
        q = deque([]); visited = set()
        for m, n, dist in points:
            q.append((m,n,dist))
            visited.add((m,n))
        dist_ans = 0
        dist_arr = []
        while q:
            i, j, dist = q.popleft()
            dist_ans = max(dist, dist_ans)
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<height and 0<=y<width and (x,y) not in visited:
                    q.append((x,y,dist+1))
                    visited.add((x,y))
        ans = min(dist_ans, ans)

    return ans

res = build(3,2,2)
print(res)