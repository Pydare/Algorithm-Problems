from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None


def leftview(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)

    while queue:

        size = len(queue)
        i = 0

        while i < size:
            curr = queue.popleft()
            i += 1
            
            if i == 1:
                print(curr.key, end=' ')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)