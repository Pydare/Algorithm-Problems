l = []
def fun(M,i,j):
    if i == len(M)-1:
        return M[i][j]
    #calculation of left sum only
    if j>0:
        l_sum = [M[i][j] + elm for elm in fun(M,i+1,j-1)]
       
    m_sum = [M[i][j] + elm for elm in fun(M,i+1,j)]
    #calculation of right sum if one's not in last column
    if j<len(M[0])-1:
        r_sum = [M[i][j] + elm for elm in fun(M,i+1,j+1)]
    #return the sum of columns as a list
    if j>0 and j<len(M[0])-1:
        return l_sum + m_sum + r_sum
    if j==0:
        return m_sum + r_sum
    if j==len(M[0])-1:
        return l_sum+m_sum

def minSliceWeight(matrix):
    global l
    for k in range(len(matrix[0])):
        slices = fun(matrix,0,k)
        for elm in slices:
            l.append(elm)
    return min(l)


l = [[1,2,3],[4,5,6],[7,8,9]]
print(minSliceWeight(l))