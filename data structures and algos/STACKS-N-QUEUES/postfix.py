from stackarray import Stack

def infix_to_postfix(infix):
    postfix = ''

    st = Stack()

    for symbol in infix:
        if symbol == ' ' or symbol == '\t': #ignore blanks and tabs
            continue
        if symbol == '(':
            st.push(symbol)
        elif symbol == ')':
            next = st.pop()
            while next != '(':
                postfix += next
                next = st.pop()
        elif symbol in '+-*/%^':
            while not st.is_empty() and precedence(st.peek()) >= precedence(symbol):
                postfix += st.pop()
            st.push(symbol)
        else: #operand
            postfix = postfix + symbol

    while not st.is_empty():
        postfix += symbol
    return postfix

def precedence(symbol):
    if symbol == '(':
        return 0
    elif symbol in '+-':
        return 1
    elif symbol in '*/%':
        return 2
    elif symbol == '^':
        return 3
    else:
        return 0

def evaluate_postfix(postfix):
    st = Stack

    for symbol in postfix:
        if symbol.isdigit():
            st.push(int(symbol))
        else:
            x = st.pop()
            y = st.pop()

            if symbol == '+':
                st.push(y + x)
            elif symbol == '-':
                st.push(y - x)
            elif symbol == '*':
                st.push(y * x)
            elif symbol == '/':
                st.push(y / x)
            elif symbol == '%':
                st.push(y % x)
            elif symbol == '^':
                st.push(y ** x)
    return st.pop()


while True:
    print("Enter the infix expression: ",end='')
    expression = input()
    if expression == 'q':
        break
    postfix = infix_to_postfix(expression)
    value = evaluate_postfix(expression)
    print('Postfix expression is: ', postfix)
    print('Value of expression: ', value)