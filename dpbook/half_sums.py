"""
142124 --> 6
9430723 --> 4
"""

def max_substring_length(s):
    n = len(s)
    max_len = 0
    summ = [[0 for _ in range(n)] for _ in range(n)]

    #lower diagonal of matrix is not used (i>j)
    for x in range(n):
        summ[x][x] = 0

    for i in range(2,n):
        for j in range(0,n-i+1):
            k = j+i-1
            l = i//2  
            #calculate value of summ[j][k]
            summ[j][k] = summ[j][k-l] + summ[k-l+1][k]
            #update if i is even, left and right sums are same and i isn't more than maxlen
            if i%2==0 and summ[j][k-l]==summ[(k-l+1)][k] and i >max_len:
                max_len = i
            
    return max_len
