class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random(head):
    if not head:
        return head
    
    ptr = head
    while ptr:

        #cloned node
        new_node = Node(ptr.val,None,None)

        #insert cloned node next to original node
        new_node.next = ptr.next
        ptr.next = new_node
        ptr = new_node.next

    ptr = head

    #linking the random pointer of new nodes based on original nodes
    while ptr:
        ptr.next.random = ptr.random.next if ptr.random else None
        ptr = ptr.next.next

    #unweave
    ptr_old = head
    ptr_new = head.next
    head_old = head.next
    while ptr_old:
        ptr_old.next = ptr_old.next.next