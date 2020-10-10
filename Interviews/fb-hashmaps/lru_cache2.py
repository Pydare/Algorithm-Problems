class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def remove_node(self,node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def add_node(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def update(self,node):
        self.remove_node(node)
        self.add_node(node)

    def insert(self,node):
        self.add_node(node)
        self.count += 1
        #return node

    def remove_last(self):
        last = self.tail.prev
        self.remove_node(last)
        self.count -= 1
        return last

class LRUCache:
    def __init__(self,capacity):
        self.dll = DLL()
        self.dic = {}
        self.cap = capacity

    def put(self,key,value):
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.dll.update(node)
        else:
            if self.dll.count == self.cap:
                last = self.dll.remove_last()
                del self.dic[last.key]
            node = Node(key,value)
            self.dic[key] = node
            self.dll.insert(node)

    def get(self,key):
        if key in self.dic:
            node = self.dic[key]
            self.dll.update(node)
            return node.val
        else:
            return -1