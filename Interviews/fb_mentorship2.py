def passwordCreation(a,b):
    s = a + b
    a_count = len(a)
    b_count = len(a) + len(b)
    s = [i for i in s]
    i,j = 0,a_count
    p = ''
    while i < a_count and j < b_count:
        p += s[i]
        i += 1
        p += s[j]
        j += 1
    while i < a_count:
        p += s[i]
        i += 1
    while j < b_count:
        p += s[j]
        j += 1
    return p
    



r = passwordCreation('seyi','adewumi')
print(r)
