
"""
A−(B+C)+(D+E−F)         stack = [)F-]
"""

def evaluate_expr(stack):
    res = stack.pop() if stack else 0

    while stack and stack[-1] != ')':
        sign = stack.pop()
        if sign == '+':
            res += stack.pop()
        else:
            res -= stack.pop()

    return res

def calculate(s):

    stack = []
    n, operand = 0,0

    for i in range(len(s)-1,-1,-1):
        ch = s[i]

        if ch.isdigit():
            operand = (10**n * int(ch)) + operand
            n += 1

        elif ch != ' ':
            if n:
                stack.append(operand)
                n, operand = 0,0

            if ch == '(':
                res = evaluate_expr(stack)
                stack.pop()

                #append the evaluated result to the stack
                stack.append(res)
            else:
                stack.append(ch)

    if n:
        stack.append(operand)
    return evaluate_expr(stack)