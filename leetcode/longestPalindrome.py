import sys

def longestPalindromicSubstring(s):
    n = len(s)
    checker = [[False for i in range(n)] for _ in range(n)]

    #filling  up the major diagonals
    for i in range(n):
        for j in range(n):
            if i == j:
                checker[i][j] = True

    #cases of length of 2
    for i in range(n-1):
        for j in range(i+1,i+2):
            if s[i] == s[j]:
                checker[i][j] = True

    #cases of length greater than 2
    for i in range(n):
        for j in range(i+2,n):
            if s[i] == s[j] and checker[i+1][j-1] == True:
                checker[i][j] = True
    i_target, j_target = sys.maxsize, -sys.maxsize
    max_diff = 0

    for i in range(n):
        for j in range(n):
            if checker[i][j] == True:
                diff = j-i
                if diff > max_diff:
                    max_diff = diff
                    i_target = i
                    j_target = j
                

    return s[i_target:j_target+1]

res = longestPalindromicSubstring('abcba')
print(res)


