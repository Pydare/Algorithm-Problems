class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

def kthLargest(root,k):
    curr = root
    klargest = None
    count = 0

    while curr != None:
        if curr.right == None:
            count += 1
            if count == k:
                klargest = curr
            curr = curr.left
        else:
            succ = curr.right
            while succ.left != None and succ.left != curr:
                succ = succ.left
            if succ.left == None:
                succ.left = curr
                curr = curr.right
            else:
                succ.left = None
                count += 1
                if count == k:
                    klargest = curr
                curr = curr.left
    return klargest