# def checkMagazine(magazine, note):
#     flag = False

#     n_len = len(note)
#     m_len = len(magazine)

#     for i in range(n_len):
#         if note[i] in magazine:
#             magazine.pop(magazine.index(note[i])) 
#             flag = True
#         elif note[i] not in magazine:
#             flag = False
#             break
#     if flag==True:
#         print('Yes')
#     elif flag==False:
#         print('No')
#     print(magazine)

def checkMagazine(magazine,note):
    x = {}
    for i in magazine:
        if x.get(i, None) is not None:
            x[i] += 1
        else:
            x[i] = 1
    for i in note:
        if i not in x:
            return "No"
        elif i in x and x[i] <= 1:
            return 'No'
        else:
            x[i] -= 1
    return 'Yes'

checkMagazine(['give','me','one','grand','today','night'],['give' 'one' 'grand' 'today'])
    
          