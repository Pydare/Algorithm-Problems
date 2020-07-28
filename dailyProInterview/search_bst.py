class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

def search_recur(root,x):

    def helper(root,x):
        if not root:
            return False
        if x == root.val:
            return True
        elif x < root.val:
            return helper(root.left,x)
        elif x > root.val:
            return helper(root.right,x)

    res = helper(root,x)
    return res

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)

ans = search_recur(root,5)
print(ans)