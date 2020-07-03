def longestChar(s):
    if s == "":
        return 0
    d = dict()
    for i in s:
        if d.get(i,None) is None:
            d[i] = 1
        else:
            d[i] += 1
    res = max(d.values())
    return res

def longestChar2(s): #optimizing my algorithm to O(1) space
    count, max_count = 1, 0
    a = sorted(s)
    if s == "":
        return 0
    for i in range(len(a)-1):
        if a[i+1] == a[i]:
            count += 1
        else:
            count = 1
        max_count = max(max_count,count)
    return max_count

ans = longestChar2('abccccdefyyyyy')
print(ans)