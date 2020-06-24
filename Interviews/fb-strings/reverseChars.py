def reverse(s):
    s = [i for i in s]
    p1,p2 = 0,len(s)-1
    while p1 < p2:
        s[p1],s[p2] = s[p2],s[p1]
        p1 += 1
        p2 -= 1

    return ''.join(s)

res = reverse('tomo rrow')
print(res)

d = 'same'
print(d[::-1])