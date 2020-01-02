def longestPalindrome(s):
    tracker = []
    for i in range(1,len(s)-1):
        left = i-1
        right = i+1
        while left>=0 and right<=len(s)-1 and s[left]==s[right]:
            left-=1
            right+=1
        tracker.append((left+1,right-1))
    dif_list = [i[1]-i[0] for i in tracker]
    max_index = dif_list.index(max(dif_list))
    a,z = tracker[max_index]
    ans = ''
    for i in range(a,z+1):
        ans += s[i]
    return ans


print(longestPalindrome('cbbd'))