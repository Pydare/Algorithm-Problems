def superDigit(n,k):
    p = int(str(n)*k)
    ans = _superDigit(p)
    return ans

def _superDigit(i):
    if len(str(i)) < 2:
        return i
    p = _superDigit(sum([int(j) for j in str(i)]))
    return p


print(superDigit(148,3))

max()