from collections import Counter
def min_window(s,t):

    if not t or not s:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t)
    l,r = 0,0
    formed = 0
    window_count = {}

    #ans tuple of form (window-length, left, right)
    ans = float('inf'), None, None

    while r < len(s):
        ch = s[r]
        window_count[ch] = window_count.get(ch,0)+1

        if ch in dict_t and window_count[ch] == dict_t[ch]:
            formed += 1

        #reduce the size from the left end
        while l <= r and formed == required:
            ch = s[l]

            #save the smallest window until now
            if r-l+1 < ans[0]:
                ans = (r-l+1,l,r)
            
            window_count[ch] -= 1
            if ch in dict_t and window_count[ch] < dict_t[ch]:
                formed -= 1
            
            l += 1
        r += 1

    return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]