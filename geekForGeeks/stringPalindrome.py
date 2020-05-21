#function to check if the string is a palindrome
def isPalindrome(s,low,high):
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True

def allPalParttUtil(allPart,currPart,start,n,s):
    #base case
    if start >= n:
        x = currPart.copy()
        allPart.append(x)
        return

    for i in range(start,n):
        if isPalindrome(s,start,i):
            currPart.append(s[start : (i+1)])

            allPalParttUtil(allPart, currPart, i+1, n, s)

            currPart.pop()

