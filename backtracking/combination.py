"""
1234
12
"""

def combine(n,k):
    
    def backtrack(temp=[],idx=1):
        if len(temp) == k:
            res.append(temp[:])

        for i in range(idx,n+1):
            #choose
            temp.append(i)
            #use next elements
            backtrack(temp,i+1)
            #backtrack
            temp.pop()
    res = []
    backtrack()
    return res
    
ans = (combine(4,2))
print(ans)