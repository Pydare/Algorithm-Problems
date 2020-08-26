from collections import defaultdict
def threeCharsDistinct(s):
    d = defaultdict(int)
    count = i = 0
    flag = True
    
    while i < len(s)-2:
        d[s[i]] += 1
        d[s[i+1]] += 1
        d[s[i+2]] += 1
        
        for k,v in d.items():
            if v != 1:
                flag = False
                break
        print(dict(d))
        if flag:
            count += 1
        d = defaultdict(int)
        print(dict(d))
            
        i += 1
        
    return count

a = ['a','b','c','d','e']
b = ['a','b','c']
c = ['d','e']
print(a[3:3])

j = 0
while j < len(c):
    a[j] = c[j]
    j += 1
k = j
l = 0
while l < len(b):
    a[k] = b[l]
    k += 1
    l += 1

#cummulativve sum of sizes [0,3,5,8,10,11]
sizes = [3, 2, 3, 1, 1]
cumm_size = [0] * (len(sizes)+1)
for i in range(1,len(cumm_size)):
    cumm_size[i] = sizes[i-1] + cumm_size[i-1]

print(cumm_size)