def backSpaceCompare(s,t):
    s = [i for i in s]
    t = [i for i in t]
    i,j = 0,0
    while i <= len(s)-1:
        if s[i] == '#' and i==0:
            s.pop(0)
        elif s[i] == '#' and i>0:
            s.pop(i-1)

        i+=1
    while j <= len(t)-1:
        if t[j] == '#' and j>0:
            t.pop(j-1)
        j+=1

    s = ''.join(s)
    t = ''.join(t)

    if s == t:
        return True
    else:
        return False

r = backSpaceCompare('a#c','b')
print(r)
