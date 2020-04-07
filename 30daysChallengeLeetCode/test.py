s = ["eat", "tea", "tan", "ate", "nat", "bat"]

p = [''.join(sorted(i)) for i in s]

d = dict()
for i in range(len(p)):
    if d.get(p[i],None) is not None:
        d[p[i]].append(i)
    else:
        d[p[i]] = [i]
l = []
for k,v in d.items():
    l.append(v)

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = s[l[i][j]]

print(l)
