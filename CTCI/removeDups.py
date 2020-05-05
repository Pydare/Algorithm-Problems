class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def remove(head):
    d = dict()
    p = head

    while p is not None:
        if p.next in d.keys():
            while p.next in d.keys():
                p.next = p.next.next
        elif p.next not in d.keys():
            p = p.next
        d[p] = 1

    return head


head = Node(8)
head.next = Node(9)
head.next.next = Node(7)
head.next.next.next = Node(6)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = Node(5)

r = remove(head)
print(r)