"""
My logic for this question is first to create a dictionary of keys that
that contains the target minus each candidate, if key in list, return both
key and value. For the multiple part, loop through each element in the 
candidates list, and find all their multiples <= target, append each multiple
and the candidate as tuples in a new list called multiples.Loop through multiples
and put in a dictionary keys, each multiple minus target. Finally loop through
candidates list,and check if value is in keys, if its in keys;divide the 
multiple by the original base number to find the number of times that element
would appear and add the element found in the key, just like the previous logic
in the beginning.
"""

def combinationSum(candidates,target):
    d,l = {},[]
    for i in candidates:
        d[target-i] = i
    for i in d.keys():
        if i in candidates:
            l.append([i,d[i]])
        if i == 0:
            l.append(d[i])
    multiples = []
    for i in candidates:
        m = i
        while m <= target:
            multiples.append((i,m))
            m += i
    d_new,adder = {},[]
    for i in multiples:
        d_new[target-i[1]] = i
    for i in d_new.keys():
        if i in candidates:
            multiplier = d_new[i][1]//d_new[i][0]
            adder = [d_new[i][0]]*multiplier
            adder.append(i)
            l.append(adder)
        #when the target is the same as multiple
        if i == 0:
            multiplier = d_new[i][1]//d_new[i][0]
            adder = [d_new[i][0]]*multiplier
            l.append(adder)
    return l

print(combinationSum([1,2,3],27))
    
            
    
        