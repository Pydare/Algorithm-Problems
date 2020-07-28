class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

"""
        60
    50       70
  40  55   65  80

40 50 55 60 65 70 80

Time complexity: O(n) and space complexity: O(n)          
"""
res = []
def smaller(root,x):

    def helper(root):
        if not root:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    j = 0
    for i in range(len(res)):
        if res[i] == x:
            j = i
            break
    for i in range(j):
        res.pop()
    return res




