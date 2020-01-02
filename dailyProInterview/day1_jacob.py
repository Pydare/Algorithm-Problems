def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    d,start = {},0
    maxx,b = 1, True
    for i in range(len(s)):
        if s[i] not in d:
            b = True
            d[s[i]] = i
        elif d[s[i]] < start:
            b = True
            d[s[i]] = i
        else:
            b = False
            maxx = max(maxx,i-start)
            start = d[s[i]] + 1
            d[s[i]] = i
    if b:
        maxx = max(maxx,i-start+1)
    return maxx


print(lengthOfLongestSubstring('pwwkew'))

