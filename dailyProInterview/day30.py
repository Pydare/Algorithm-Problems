class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.level = 0

# need to use level and 2^level
def minimum_level_sun(root):
    q = [root]
    summ = []
    while q:
        x = 0
        marx = len(q)
        for i in range(marx):
            temp = q.pop(0)
            x += temp.val
            if temp.left and (not temp.right):
                q.append(temp.left)
            if temp.right and (not temp.left):
                q.append(temp.right)
            if temp.left and temp.right:
                q.append(temp.left)
                q.append(temp.right)
        summ.append(x)
    return min(summ)

root = Node(10)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(1)
root.right.right = Node(2)

print(minimum_level_sun(root))


    