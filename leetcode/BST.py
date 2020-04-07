class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)

def deleteIter(root,x):
    root = _deleteIter(root,x)

def _deleteIter(p,x):
    par = None
    while p is not None:
        if x == p.val:
            break 
        par = p
        if x < p.val:
            p = p.left
        if x > p.val:
            p = p.right
    if p == None:
        print(x,' is not found')
        return

    #deleting p from the tree
    # case 2: p has two children
    if p.left and p.right:
        #find the inorder successor
        s = p.right
        ps = p 
        while s.left is not None:
            ps = s
            s = s.left
        p.val = s.val
        par = ps
        p = s 
    #case 1 or 0: if p has 0 or 1 child
    if p.left:
        ch = p.left
    elif p.right:
        ch = p.right
    else:
        ch = None
    #if there's no child, ch would be none
    if par.left:
        par.left = ch
    elif par.right:
        par.right = ch

def deleteRecur(root,x):
    root = _deleteRecur(root,x)

def _deleteRecur(p,x):
    if p is None:
        return 
    if x < p.val:
        p.left = _deleteRecur(p.left,x)
    elif x > p.val:
        p.right = _deleteRecur(p.right,x)
    else:
        #if it has 2 kids
        if p.left and p.right:
            s = p.right
            ps = p
            while s.left is not None:
                ps = s
                s = s.left
            p.val = s.val
            p.right = _deleteRecur(p.right,s.val)
        else:
            if p.left:
                ch = p.left
            else:
                ch = p.right
            p = ch
    return p 





root = Node(70)
root.left = Node(40)
root.left.left = Node(35)
root.left.right = Node(50)
root.right = Node(80)
root.right.left = Node(75)
root.right.right = Node(89)
root.right.right.left = Node(82)
root.right.right.right = Node(93)

inorder(root)
print()
deleteRecur(root,89)
print('After deletion')
inorder(root)
