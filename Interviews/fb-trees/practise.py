class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

def is_valid(root):

    def helper(node, lower=-float('inf'), upper=float('inf')):
        if not node:
            return True

        val = node.val
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left,lower,val):
            return False

        return True

    return helper(root)

"""
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
idx_map = {3:1,9:0,20:3,15:2,7:4}
"""


def build_tree(preorder, inorder):

    def helper(left, right):
        nonlocal pre_idx

        if left == right:
            return None

        root_val = preorder[pre_idx]
        root = Node(root_val)

        index = idx_map[root_val]

        pre_idx += 1
        root.left = helper(left,index)
        root.right = helper(index+1,right)
        return root

    pre_idx = 0
    idx_map = {val:idx for idx,val in enumerate(inorder)}
    return helper(0,len(preorder))


