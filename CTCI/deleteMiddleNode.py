class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def deleteMiddle(head):

    def count(head):
        p = head
        count = 1
        while p.next is not None:
            p = p.next
            count += 1
        return count

    total = count(head)
    position = total//2
    c = 0 #or 1
    p = head
    while p.next is not None:
        if count == position-1:
            p = p.next.next
            count += 1
        else:
            p = p.next
            count += 1
    return p 