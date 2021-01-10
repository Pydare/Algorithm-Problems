def longest_common_subsequence(s, t):
    m, n = len(s), len(t)
    memo = [[-1 for _ in range(m)] for _ in range(n)]
    def helper(s, t, m, n):
        if m == 0 or n == 0:
            return 0
        if memo[m][n] != -1:
            return memo[m][n]
        # comparing the last character of recursion
        if s[m-1] == t[n-1]:
            memo[m][n] =  1 + helper(s, t, m-1, n-1)
        else:
            memo[m][n] = max(helper(s, t, m, n-1), helper(s, t, m-1, n))

        return memo[m][n]

    return helper(s, t, m, n)

#DP solution
def lcs_dp(s,t):
    m,n = len(s),len(t)
    res = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                res[i][j] = res[i-1][j-1] + 1
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])
   
    def print_lcs(s,t,m,n):
        length = res[m][n]
        #array to store the char in LCS
        c = ["0"]*length
        i, j = m, n
        while i > 0 and j > 0:
            #if current character in s and t are equal
            if s[i] == t[j]:
                c[length] = s[i]
                length -= 1
                i -= 1
                j -= 1
            #if not equal, find larger of the 2 and go in direction of larger value
            elif res[i-1][j] > res[i][j-1]:
                i -= 1
            else:
                j -= 1
        return ''.join(c)
    
    word = print_lcs(s,t,m,n)
    return res[m][n], word

ans,word = lcs_dp('ABCD','AEBD')
print(ans,word)