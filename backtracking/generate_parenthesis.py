'''
((()))
(()())
(())()
()(())
()()()
boat ---> boat, bota, 

generate all possible arrangements and have a valid parenthesis condition
'''

def parenthesis_permutation(n):
    s = '('*n + ')'*n 
    s = [i for i in s]
    res = []
    def helper(s,temp):
        if not s and is_valid(temp) and ''.join(temp) not in res:
            res.append(''.join(temp))
        else:
            for i in range(len(s)):
                c = s[i]
                temp.append(c)
                s.remove(c)
                helper(s,temp)
                s.insert(i,c)
                temp.pop()
    helper(s,[])
    return res

def is_valid(temp):
    stack = []
    i = 0
    while i < len(temp):
        if temp[i] == '(':
            stack.append(temp[i])
        elif temp[i] == ')':
            if not stack:
                return False
            else:
                stack.pop()
        i += 1

    if not stack:
        return True
    else:
        return False

res = parenthesis_permutation(3)
print(res)
        



         
