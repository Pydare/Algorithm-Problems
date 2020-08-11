class Node:
    def __init__(self,val):
        self.val = val
        self.head = None
        self.next = None

def reorder_list(head,tail):
    count = 0
    p = head
    while p.next is not None:
        count += 1
        p = p.next

    