def hash(s,words):
    hash_table = {}
    for word in words:
        for c in word:
            if c not in hash_table:
                hash_table[c] = 1
            else:
                hash_table[c] += 1
    return hash_table

def findSubstring(s,words):
 
    res = []
    hash_table = {}
    check_length = len(words[0]) * len(words)
    hash_table = hash(s,words)
                
    curr, i = 0, 0
    temp_ht = hash_table
    while i < len(s):
        print(curr,i,temp_ht)
        if s[i] in temp_ht:
            temp_ht[s[i]] -= 1
        if i-curr == check_length-1:
            if all(v==0 for k,v in temp_ht.items()):
                res.append(curr)
            curr += 1
            i = curr 
            temp_ht = hash(s,words)
            continue
        
        i += 1
    return res

ans = findSubstring("barfoofoobarthefoobarman",["bar","foo","the"])
print(ans)