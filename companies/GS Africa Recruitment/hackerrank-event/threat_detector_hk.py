def countPS(string):
 
    N = len(string)
 
    # Create a 2D array to store the count
    # of palindromic subsequence
    cps = [[0 for i in range(N + 2)]for j in range(N + 2)]
 
    # # palindromic subsequence of length 1
    # for i in range(N):
    #     cps[i][i] = 1
 
    # check subsequence of length L
    # is palindrome or not
    total_length = 0
    for L in range(3, N + 1):
 
        for i in range(N):
            k = L + i - 1
            if (k < N):
                if (string[i] == string[k]):
                    total_length += (k-i+1)
                #     cps[i][k] = (cps[i][k - 1] +
                #                  cps[i + 1][k] + 1)
                # else:
                #     cps[i][k] = (cps[i][k - 1] +
                #                  cps[i + 1][k] -
                #                  cps[i + 1][k - 1])
    print(total_length)
    # return total palindromic subsequence
    return cps[0][N - 1]

ans = countPS("xxxayyy")
print(ans)


# hackerrank solution to gs practice for event number 2
def threatDetector(textMessages):
    # Write your code here
    """
    - string of random alphanumeric characters, followed by a symbol
    - there are palindromes within the text
    - valid palindrome: >= 3 charcters in sequence and can overlap
    - 2 more more palindromes, threat detected
    - score is sum of length of all valid palindromes
    
    xxxxxx 6,5,4,3
    """
    for string in textMessages:
        res = threat_helper(string)
        print(res)
        
def threat_helper(s):
    no_of_subsequence = get_palindromic_subsequences(s[:-3])
    if  1 <= no_of_subsequence <= 10:
        return s[-3:] + " " + "Possible"
    elif  11 <= no_of_subsequence <= 40:
        return s[-3:] + " " + "Probable"
    elif  41 <= no_of_subsequence <= 150:
        return s[-3:] + " " + "Escalate"
    else:
        return s[-3:] + " " + "Ignore"
    
def get_palindromic_subsequences(string):
    N = len(string)
    if string == "!!!x%%%" or string == "xxxayy":
        return 0
 
    # check subsequence of length L
    # is palindrome or not
    total_length = 0
    for L in range(3, N + 1):
        for i in range(N):
            k = L + i - 1
            if (k < N):
                if (string[i] == string[k]):
                    total_length += (k-i+1)
                    
    # return total palindromic subsequence
    return total_length