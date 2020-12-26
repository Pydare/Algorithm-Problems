def smallest_division(s, t):
    tcopy = t
    len_s, len_t = len(s), len(t)

    def repeater(s):
        i = (s+s)[1:-1].find(s)
        if i == -1:
            return s
        else:
            return s[:i+1]

    while len_s > len_t:
        t = tcopy + t
        len_t = len(t)

    if s == t:
        rt = repeater(t)
        return len(rt)
    else:
        return -1

ans = smallest_division("gcdgcdgcdgcdgcdgcd", "gcdgcd")
print(ans)