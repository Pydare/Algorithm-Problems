def sub_palindromes(s):
    """
    mokkori
    """
    palindromes = set()

    for i in range(len(s)):
        # for odd cases
        get_palindromes(s,i,i,palindromes)
        # for even cases
        get_palindromes(s,i,i+1,palindromes)

    return list(palindromes)
        

def get_palindromes(s,l,r,palindromes):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        palindromes.add(s[l:r+1])
        l -= 1
        r += 1

res = sub_palindromes('mokkori')
print(res)

# dp solution: https://www.geeksforgeeks.org/count-palindrome-sub-strings-string/