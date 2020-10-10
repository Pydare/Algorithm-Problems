def prison(n,m,h,v):
    #the trick is to find the length of max gaps horizontally
    #and vertically
    x = [1]*(n+1)
    y = [1]*(m+1)
    cx,ox,cy,oy = 0,float('-inf'),0,float('-inf')

    for i in range(len(h)):
        x[h[i]] = 0 #x has 1 where there is a bar and 0 for removed bar
    
    for i in range(len(v)):
        y[h[i]] = 0 #y has 1 where there is a bar and 0 for removed bar

    #loop to find the max gap horizontally
    for i in range(1,n):
        if x[i] == 1:
            cx = 0
        else:
            cx += 1
            ox = max(ox,cx)

    #loop to find the max gap vertically
    for i in range(1,m):
        if y[i] == 1:
            cy = 0
        else:
            cy += 1
            oy = max(oy,cy)

    return (ox+1) * (oy+1)

res = prison(3,3,[2],[2])
print(res)