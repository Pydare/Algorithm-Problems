class Node:
    def __init__(self,value):
        self.value = value
        self.link = None

def insertNode(head, valueToInsert):
    p = head
    temp = Node(valueToInsert)
    while p.link is not None:
        p.link = temp
        temp.link = None
        p = p.link
        return p

node1 = Node('3')
node2 = Node('4')
node3 = Node('5')

node1.link = node2
node2.link = node3

a = insertNode(node1, '7')
print(a)