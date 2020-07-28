class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class Dll:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,1)      #head<->(-1,-1) ... (-1,-1)<->tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def remove_node(self,node):
        pre,nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def add_node(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def update(self,node):
        self.remove_node(node)
        self.add_node(node)

    def insert(self,node):
        self.add_node(node)
        self.count += 1
        return node #return node to add it to a hashmap

    def remove_last(self):
        last = self.tail.prev
        self.remove_node(last)
        self.count -= 1
        return last #return node to remove it to a hashmap


class LRUCache:
    def __init__(self,capacity):
        self.dll = Dll()
        self.dic = {}
        self.cap = capacity

    def get(self,key):
        if key in self.dic:
            node = self.dic[key]
            self.dll.update(node)
            return node.value
        else:
            return -1

    def put(self,key,value):
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            self.dll.update(node)
        else:
            if self.dll.count == self.cap:
                last = self.dll.remove_last()
                del self.dic[last.key]
            node = Node(key,value)
            self.dic[key] = node
            self.dll.insert(node)
