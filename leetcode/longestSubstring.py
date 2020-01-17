import numpy as np
def lengthOfLongestSubstring(s):
        rowlength = len(s)
        table = np.ones((rowlength,rowlength), dtype=np.int32)
        m = 0
        for i in range(1,len(s)):
            for j in range(1,len(s)):
                if s[i-1] == s[j-1]:
                    table[i][j] = table[i-1][j-1]+1
                    if m < table[i][j]:
                        m = table[i][j]
                    elif s[i-1] == s[j-1] and s[i] == s[j]:
                        table[i][j] = 1
                        m = 1
                        
        return s[0]


print(lengthOfLongestSubstring('pwwkew'))