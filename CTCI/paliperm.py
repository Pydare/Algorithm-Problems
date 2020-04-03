def check(s):
    d = dict()
    for i in range(len(s)):
        if d.get(s[i],None) is None:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    count = 0
    for _,v in d.items():
        if v != 2 and v != 1:
            return False
        elif v == 1:
            count += 1
    if count > 1:
        return False
    return True


print(check('ssddffttuuiipppeeoo'))