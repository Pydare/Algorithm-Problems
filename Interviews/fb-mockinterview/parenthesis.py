def generate_parenthesis(n):

    ans = []

    def backtrack(s="",left=0,right=0):
        print(s)
        if len(s) == 2*n:
            ans.append(s)
            return
        if left < n:
            backtrack(s+"(",left+1,right)
        if right < left:
            backtrack(s+")",left,right+1)

    backtrack()
    return ans

res = generate_parenthesis(3)
print(res)