def evalRPN(tokens):
    stack = []
        
    for ch in tokens:
        print(stack)
        if ch.isdigit():
            stack.append(int(ch))
        elif ch in ["+","-","*","/"]:
            operator = ch
            r = tokens.pop()
            l = tokens.pop()
            if operator == "+":
                res = l+r
            elif operator == "-":
                res = l-r
            elif operator =="/":
                res = l//r
            else:
                res = l*r
            stack.append(res)
            
    return stack.pop()

ans = evalRPN(["2", "1", "+", "3", "*"])
print(ans)