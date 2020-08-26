class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None
        self.left_size = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def add_helper(self,root,num):
        if not root:
            root = TreeNode(num)
            return root
        if num <= root.val:
            root.left = self.add_helper(root.left,num)
            root.left_size += 1
        else:
            root.right = self.add_helper(root.right,num)
        return root

    def add(self,num):
        self.root = self.add_helper(self.root,num)
        self.count += 1

    def rank(self,k):
        return self.rank_helper(self.root,k)

    def rank_helper(self,root,k):
        if not root:
            return -1
        if root.left_size == k:
            return root.val
        if root.left_size > k:
            return self.rank_helper(root.left,k)
        else:
            return self.rank_helper(root.right, k-root.left_size-1)

class MedianFinder:
    def __init__(self):
        self.bst = BinarySearchTree()

    def add_num(self, num):
        self.bst.add(num)

    def find_median(self):
        #size of elements
        size = self.bst.count
        if size % 2 == 0:
            rank1 = self.bst.rank(size//2)
            rank2 = self.bst.rank(size//2-1)
            return (rank1+rank2)/2
        else:
            return self.bst.rank(size//2)