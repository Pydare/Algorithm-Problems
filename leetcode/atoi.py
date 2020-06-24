import re

def myAtoi(str):
        
    #too much condtions sigh
    #1. can be white space before the first non-white space which would be -,+ or integer, return the int
    #2. the addtional characters after #1. are ignored
    #3. if the first non-white character is not a number, return 0
    #4. if the number isn't in the range -2^31, 2^31-1, return either of them depending
    
    max_n, min_n = (2**31-1), -(2**31)
    d = dict()
    for i in range(10):
        d[i] = 1
    
    #striping the string
    str = str.strip()
    
    #condtion #3
    if int(str[0]) not in d:
        if str[0] != "+" or str[0] != "-":
            return 0
        
    #spliting into a list       
    str_list = str.split()
    
    #checking if all the numbers are integers or -,+
    for i in str_list[0]:
        if int(i) not in d:
            if i != '-' or i != '+':
                return 0
            
    #turning back into a string        
    res = ''.join(str_list[0])
    if res[0] == '-':
        ans =  -int(res[1:])
    elif res[0] == '+':
        ans = +int(res[1:])
    else:
        ans = int(res)
    
    #checking the finsl condition for sys max and min
    if ans < min_n:
        return min_n
    elif ans > max_n:
        return max_n
    else:
        return ans


def myAtoiRE(s):
    s = str.lstrip()        
    potential_nums = re.findall("[\+\-]{0,1}[0-9]+", s)
    
    if len(potential_nums) == 0:
        return 0
    if not s[0].isnumeric():
        if s[0] not in ['+', '-'] or not s[1].isnumeric():
            return 0
    
    return min(max(int(potential_nums[0]), -(2 ** 31)), 2 ** 31 - 1)

res = myAtoiRE("42")
print(res)