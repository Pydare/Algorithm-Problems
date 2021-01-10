import functools

def count_palindromic_subsequence(string):

    def helper(i, j):
        # every character of a string is a palindrome
        if i == j:
            return 1
        
        # if the first and last characters are the same
        # consider it as palindrome subsequence and check
        # for the rest subsequence (i+1, j), (i, j-1)
        elif string[i] == string[j]:
            return  1 + helper(i+1, j) + helper(i, j-1)

        # check for rest subsequence and remove common
        # palindromic subsequences as they're counted
        # twice when we do helper(i+1, j) + helper(i, j-1)
        else:
            return helper(i+1, j) + helper(i, j-1) - helper(i+1, j-1)

    return helper(0, len(string) - 1)

# ans = count_palindromic_subsequence("aaaaa")
# print(ans)

# cache the result of subproblems using top-down appraoch
def count_palindromic_subsequence_topdown(string):

    cache = {}
    def helper(i, j):
        # every character of a string is a palindrome
        if i == j:
            return 1

        # check if string in cache
        if string[i:j+1] in cache:
            return cache[string[i:j+1]]
        
        # if the first and last characters are the same
        # consider it as palindrome subsequence and check
        # for the rest subsequence (i+1, j), (i, j-1)
        elif string[i] == string[j]:
            cache[string[i:j+1]] =  1 + helper(i+1, j) + helper(i, j-1)

        # check for rest subsequence and remove common
        # palindromic subsequences as they're counted
        # twice when we do helper(i+1, j) + helper(i, j-1)
        else:
            cache[string[i:j+1]] = helper(i+1, j) + helper(i, j-1) - helper(i+1, j-1)

        # return cache
        return cache[string[i:j+1]]

    return helper(0, len(string) - 1)

ans = count_palindromic_subsequence_topdown("aaaaa")
print(ans)


# dynamic programming solution
def count_palindromic_subsequence_dp(string):
    n = len(string)

    # create a 2d array to store the count of palindromic subsequence
    dp = [[0 for i in range(n + 2)] for j in range(n + 2)]

    # palindromic subsequence of length 1
    for i in range(n):
        dp[i][i] = 1

    # check if subsequence of length L is palindrome or not
    for L in range(2, n+1):
        for i in range(n):
            k = L + i - 1
            if k < n:
                if string[i] == string[k]:
                    dp[i][k] = 1 + dp[i][k-1] + dp[i+1][k]
                else:
                    dp[i][k] = dp[i][k-1] + dp[i+1][k] - dp[i+1][k-1]

    # return total palindromic subsequence
    return dp[0][n-1]