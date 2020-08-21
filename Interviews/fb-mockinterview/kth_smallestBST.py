class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthelement(root,k):
    
    def helper(root,k):
        if not root:
            return k
        helper(root.left,k)
        k += 1
        if res == k:
            return root.val

    return helper(root,k)

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

ans = kthelement(root,1)
print(ans)