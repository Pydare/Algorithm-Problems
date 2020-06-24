def delete(s,c):
    s = [i for i in s]
    n = len(s)
    i, count = 0, 0

    #counting the occurences of c in the string
    for k in s:
        if k == c:
            count += 1

    #edge case
    if count == 0:
        return ''.join(s)

    #re-assigning the indices of characters that are not c
    for j in range(n):
        if s[j] != c:
            s[i] = s[j]
            i += 1

    #assigning the rest of the character c, to the end of the list
    new_index = n - count
    for i in range(count):
        s[new_index + i] = c
    
    #popping the characters c in the list
    for i in range(count):
        s.pop()
    
    return ''.join(s)    


ans = delete('rcticgsc','c')
print(ans)

# one could use the built in string.translate() method  