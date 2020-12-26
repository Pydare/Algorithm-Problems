def boundaryOfBinaryTree(root):
        
    """
    1. empty = []
    2. root = [root.val]
    3. skewed trees = [all values] (left or right)
    """
    def is_leaf(node):
        return not node.left and not node.right
    
    res = []
    if not root:
        return res
    
    if not is_leaf(root):
        res.append(root.val)

    def add_leaves(node):
        if not node.left and not node.right:
            res.append(node.val)
        if node.left:
            add_leaves(node.left)
        if node.right:
            add_leaves(node.right)

    left_t = root.left
    while left_t is not None:
        if not is_leaf(left_t):
            res.append(left_t.val)
        if left_t.left:
            left_t = left_t.left
        else:
            left_t = left_t.right

    add_leaves(root)

    stack = []
    right_t = root.right
    while right_t is not None:
        if not is_leaf(right_t):
            stack.append(right_t.val)
        if right_t.right:
            right_t = right_t.right
        else:
            right_t = right_t.left

    while stack:
        res.append(stack.pop())

    return res