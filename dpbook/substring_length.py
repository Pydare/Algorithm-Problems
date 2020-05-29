def maxSubStringLength(s):
    n = len(s)
    maxLen = 0

    # i = starting index of substring
    for i in range(n):
        # j = end index of substring (even length)
        for j in range(i+1,n,2):
            # len = length of current substring
            length = j - i + 1

            #if maxLen > length of current string, do nothing
            if maxLen >= length:
                continue
            
            lsum,rsum = 0,0
            for k in range(length//2):
                lsum += int(s[i+k]) - int('0')
                rsum += int(s[i+k+length//2]) - int('0')

            if lsum == rsum:
                maxLen = length

    return maxLen

def maxSubStringLength2(s):
    n = len(s)
    summ = [[0 for i in range(n)] for _ in range(n)]
    maxLen = 0

    #lower diagonal of matrix is not used
    for i in range(n):
        summ[i][i] = int(s[i])
    
    for length in range(2,n):
        for i in range(n-length+1):
            j = i + length - 1
            k = length//2

            #calculate the value of sum[i][j]
            summ[i][j] = summ[i][j-k] + summ[j-k+1][j]

            #update if length is even, left and right
            #sums are same and length is more than maxLen
            if (len%2==0 and summ[i][j-k]==summ[j-k+1][j] and len > maxLen):
                maxLen = length

    return maxLen