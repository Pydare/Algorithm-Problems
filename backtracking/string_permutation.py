def permute(s):
    s = [i for i in s]

    def helper(s,temp):
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

print(permute('DARE'))