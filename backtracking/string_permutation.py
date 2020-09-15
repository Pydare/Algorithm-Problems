def permute(s):
    s = [i for i in s]

    def helper(s,temp):
        print(s,temp)
        #base case
        if not s:
            print(''.join(temp))
        else:
            for i in range(len(s)):
                #choose 
                c = s[i]
                temp.append(c)
                s.remove(c)
                #explore
                helper(s, temp)
                #unchoose
                s.insert(i,c)
                temp.pop()

    helper(s,[])

def permute_optimised(s):
    s= list(s)
    res = []
    def helper(s,idx):
        if idx == len(s):
            res.append(''.join(s))
        else:
            for i in range(idx,len(s)):
                #choose
                s[i], s[idx] = s[idx], s[i]
                helper(s,idx+1)
                s[i], s[idx] = s[idx], s[i]
    helper(s,0)
    return res

print(permute_optimised('abc'))

##itertools way
from itertools import permutations
perm_list = permutations('ABC')
for perm in perm_list:
    print(''.join(perm))


#print(permute_optimised('ABC'))