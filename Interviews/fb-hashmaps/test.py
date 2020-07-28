from copy import deepcopy, copy
s1 = 'playboy'
s2 = s1
ustring = u'A unicode \u018e string \xf1'

s = ustring.encode('utf-8')

l = [True,True,False,True,True,False,False]
print(l[2:4:2])