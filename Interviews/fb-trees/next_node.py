class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

def find_right_node(root,value,level,value_level):
    #return none if tree is empty
    if not root:
        return None, value_level

    #if node is found, set value_level to current level
    if root.data == value:
        return None, level

    #if value_level is already set, current node is the next right node
    elif value_level:
        if level == value_level:
            return root, level

    #recur for left subtree by increasing level by 1
    left, value_level = find_right_node(root.left, value, level+1, value_level)

    #if node is found in left subtree, return it
    if left:
        return left, value_level
    #recur in right subtree
    return find_right_node(root.right, value, level+1, value_level)

def find_right(root,value):
    value_level = 0
    return find_right_node(root,value,1,value_level)[0] 