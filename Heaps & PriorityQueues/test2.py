class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthSmallest(root,k):
        
    ret = [-1]
    def helper(root,count):
        if not root:
            return
        helper(root.left,count)
        count[0] += 1
        if count[0] == k:
            ret[0] = root.val
            return
        helper(root.right,count)
        
        
                
    helper(root,[0])
    return ret[0]

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

print(kthSmallest(root,2))