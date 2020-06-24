import re, string
def tokenizeStr(s):
    exclude = set(string.punctuation)
    s = ''.join(ch for ch in s if ch not in exclude)
    return s

ans = tokenizeStr('this man, he has a lot of problem. why not')
print(ans)