Return whether the given string, ignoring punctuation and capitalization, is a palindrome.
general postiveexample - race car
edge case - ""
edge case - 'c'
 
    Will the string fit in memory
    can i asummed that input in alwasy string


                        "lkj.hjk,L"
        
Time complexity - O(N)
Space complexity - O(1)

                             ^^

def is_char(s):
    if 'a' <= s.lower() <='z':
        return True
    else:
        return False


def is_palindrome(s): #aa1,Baa
    
    i, j = 0, len(s)-1 #1,2
    
    while i < j:
        
        if not is_char(s[i]): # a
            i += 1
            continue
            a
        if not is_char(s[j]): # a
            j -= 1
            continue
            
        
        if s[i].lower() != s[j].lower():
            return False
        
        i += 1
        j -= 1
    
    return True
        
        



