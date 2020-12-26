from collections import deque
class Solution:
    # recursive
    def isSymmetric(self, root):
        if not root:
            return True
        def isMirror(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return (root1.val == root2.val) and isMirror(root1.right,root2.left)\
            and isMirror(root1.left,root2.right)
        
        return isMirror(root.left,root.right)

    # iterative
    def isSymmetric2(self, root):
        if not root:
            return True
        
        q = deque()
        q.append(root)
        q.append(root)
        
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            
            if not t1 and not t2: continue
            if not t1 or not t2: return False
            if t1.val != t2.val: return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
            
        return True