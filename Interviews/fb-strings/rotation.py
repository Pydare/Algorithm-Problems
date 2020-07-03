def isRotation(s1,s2):
    s2 = s2+s2
    if isSubstring(s1,s2):
        return True
    else:
        return False

def isSubstring(s1,s2):
    m = len(s1)
    n = len(s2)
    flag = False
    for i in range((n-m)+1):
        for j in range(m):
            if s2[i+j] == s1[j]:
                flag = True
                if flag==True and j==m-1:
                    return True
            else:
                flag = False
    return False
            
    


ans = isSubstring('ath', 'catholic')
print(ans)
# res = isRotation('waterbottle','erbottlewat')
# print(res)