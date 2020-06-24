def isAnagram(s1,s2):
    new_s = s1+s2
    d = dict()

    for i in range(len(new_s)):
        if d.get(new_s[i], None) is None:
            d[new_s[i]] = 1
        else:
            d[new_s[i]] += 1
    for _,v in d.items():
        if v % 2 != 0: #even
            return False
    return True

res = isAnagram('abccde','baedcc')
print(res)