class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] # "([)]"
        i = 0
        
        def closing_half(close, open_):
            if close == ')' and open_ == '(':
                return True
            if close == ']' and open_ == '[':
                return True
            if close == '}' and open_ == '{':
                return True
            return False
        
        while i < len(s):
            if stack and closing_half(s[i], stack[-1]):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
                
        return True if not stack else False