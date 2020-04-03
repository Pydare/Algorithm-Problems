class Et:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#checking if c is an operator
def isOperator(c):
    if (c=='+' or c=='-' or c=='*' or c=='/' or c=='^'):
        return True
    else:
        return False
#inorder traversal function
def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.value)
        inorder(t.right)

#returns root of constructed tree for postfix expression
def constructTree(postfix):
    stack = []

    for char in postfix:
        #if operand, push into stack
        if not isOperator(char):
            t = Et(char)
            stack.append(t)
        else:
            #pop two top nodes
            t = Et(char)
            t1 = stack.pop()
            t2 = stack.pop()

            #make them children
            t.right = t1
            t.left = t2

            #add subexpression to stack
            stack.append(t)
        #only element left would be the root
        t = stack.pop()
        return t