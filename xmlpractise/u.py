from collections import Counter
lis = [1,2,3,4,1,2,6,7,3,8,1]

s = dict(Counter(lis))


print(s[1])