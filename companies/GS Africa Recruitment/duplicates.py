class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def remove_duplicates(head):
    
    # sort the list using merge sort
    def sort(head):
        if not head or not head.next:
            return head
        fast, slow, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            pre, slow = slow, slow.next
        pre.next = None
        left, right = sort(head), sort(slow)
        return merge(left, right)

    def merge(left,right):
        if not left or not right:
            return left or right
        dummy = p = Node(0)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return dummy.next

    # removal of duplicates
    head = sort(head)
    dummy = p = Node(0)
    dummy.next = head

    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            p.next = head
            p = p.next
        else:
            p.next = head
            p = p.next
        head = head.next
    
    return dummy.next

head = Node(3)
head.next = Node(4)
head.next = Node(3)
head.next = Node(2)
head.next = Node(6)
head.next = Node(1)
head.next = Node(2)
head.next = Node(6)

res = remove_duplicates(head)
while res:
    print(res.val)
    res = res.next

    