class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

"""
1->2->3->4->5->6
n = 3

n = 0, n = len(list), n in btw
"""

def insert(head,val,n):
    temp = Node(val)
    count = 0

    if n == 0:
        temp.next = head
        head = temp
    
    p = head
    while p.next is not None:
        count += 1
        if count == n:
            if p.next is None:
                p.next = temp
            else:
                temp.next = p.next
                p.next = temp
        p = p.next