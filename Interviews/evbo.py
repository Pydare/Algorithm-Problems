def editDistance(s1,s2):
    count = 0
    s1 = [i for i in s1]
    s2 = [i for i in s2]
    #dealing with their lengths
    if len(s1) < len(s2):
        diff = len(s2) - len(s1)
        for i in range(diff):
            s1.append('')
    if len(s2) < len(s1):
        diff = len(s1) - len(s2)
        for i in range(diff):
            s2.append('')
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            s1[i] = s2[i]
        if s2[i] == '':
            s1.pop(i)
        if s1[i] == '':
            s1[i] = s2[i]
        count += 1
    new_s1 = ''.join(s1)
    print(new_s1)
    print(count)
    

editDistance('horse','ros')
