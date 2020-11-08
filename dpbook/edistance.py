def edit_distance(s1,s2,i,j):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    if s1[i] == s2[j]:
        return edit_distance(s1,s2,i+1,j+1)

    #find the edit distance for all 3 operations
    d = edit_distance(s1,s2,i+1,j)
    u = edit_distance(s1,s2,i+1,j+1)
    i = edit_distance(s1,s2,i,j+1)

    #return the minimum of the 3 values plus 1
    return min(d,u,i) + 1


def edit_distance_dp(s1,s2):
    edit = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    m,n = len(edit), len(edit[0])

    for i in range(m):
        edit[i][0] = i

    for j in range(n):
        edit[0][j] = j

    for i in range(1,m):
        for j in range(1,n):
            if s1[i-1] == s2[j-1]:
                edit[i][j] = edit[i-1][j-1]
            else:
                edit[i][j] = 1 + min(edit[i-1][j-1],edit[i-1][j],edit[i][j-1])
    
    return edit[m-1][n-1]

res = edit_distance_dp('cat','car')
print(res)
