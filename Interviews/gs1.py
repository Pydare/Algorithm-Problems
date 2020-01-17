def encoding(s):
    d,p = {}, ''
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    for k,v in d.items():
        p += str(v)
        p += k
    return p

print(encoding('rrrryye'))