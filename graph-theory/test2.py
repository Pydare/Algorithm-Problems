def remove(s):
    indexes_to_remove = set()
    stack = []
    for i,c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif not stack: #if we come across ) and the stack is empty
            indexes_to_remove.add(i)
        else: #if we come across ) and there is a ( in the stack
            stack.pop()
    print(indexes_to_remove,'   ',stack)
    indexes_to_remove = indexes_to_remove.union(set(stack))
    string_builder = []
    for i,c in enumerate(s):
        if i not in indexes_to_remove:
            string_builder.append(c)
    return ''.join(string_builder)

res = remove("l(e)))et((co)d(e")
print(res)
