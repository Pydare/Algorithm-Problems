class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def remove_duplicates(head):

    previous_node = head
    current_node = previous_node.next
    keys = set([previous_node.val])

    while current_node:
        data = current_node.val

        if data in keys:
            #this is duplicate node, so discard it
            previous_node.next = current_node.next
            current_node = current_node.next
        else:
            #put the node data in keys set and move forword
            keys.add(data)
            previous_node = current_node
            current_node = current_node.next

    while head:
        print(head.val)
        head = head.next

    return head

def remove_duplicates2(head):
    if head is None:
            return None

    curr = head
    while curr is not None:
        inner = curr
        while inner.next is not None:
            if inner.next.val == curr.val:
                inner.next = inner.next.next
            else:
                inner = inner.next
        curr = curr.next
    
    return head


head = Node(3)
head.next = Node(4)
head.next = Node(3)
head.next = Node(2)
head.next = Node(6)
head.next = Node(1)
head.next = Node(2)
head.next = Node(6)

res = remove_duplicates(head)
print(res)