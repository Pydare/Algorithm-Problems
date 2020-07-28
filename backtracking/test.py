
'''
ABCD
AB AC AD BA BC BD CA CB CD DA DB DC ----> Permutation (the order doesn't matter)

AB AC AD BC BD CD -------> Combination (the order matters)

'''

"""
aab
a==
"""
def letterCasePermutation(S):
    res = []
        
    def backtrack(temp="",i=0):
        if len(temp) == len(S):
            res.append(temp)
        else:
            if S[i].isalpha():
                backtrack(temp + S[i].swapcase(), i+1)
            backtrack(temp + S[i],i+1)
    backtrack()
    return res