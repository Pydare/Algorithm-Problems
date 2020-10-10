def partition(s):
    """
    aab
    a a b aa b a ab       
    """
    if not s:
        return [[]]
    
    def helper(s,sub):
        if len(s) == 0:
            res.append(sub)
            return 
        print(sub)
        for i in range(1,len(s)+1):
            if s[:i] == s[i-1::-1]:
                helper(s[i:],sub + [s[:i]])
                
    res = []
    helper(s,[])
    return res

ans = partition('aab')
print(ans)

a = {1,2,3,4,5}
a.remove(5)