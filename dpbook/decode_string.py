class Solution:
    def __init__(self):
        self.memo = {}

    def num_decodings(self,s):
        if not s:
            return 0
        return self.recursive_with_memo(0,s)

    def recursive_with_memo(self,index,s):
        #if you reach the end of the string, return 1
        if index == len(s):
            return 1

        #if the string starts with zero, it cant be decoded
        if s[index] == '0':
            return 0
        
        #for the 2-idx checks
        if index == len(s)-1:
            return 1

        #memoization is needed
        if index in self.memo:
            return self.memo[index]

        ans = self.recursive_with_memo(index+1,s) + self.recursive_with_memo(index+2,s) if (int(s[index:index+2]) <= 26) else 0

        self.memo[index] = ans

        return ans

res = Solution()
ans = res.num_decodings('123')
print(ans)