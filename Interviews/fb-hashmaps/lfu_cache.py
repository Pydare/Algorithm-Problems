#remove the least frequently usedclass Node:
class Node:
    def __init__(self,key,val,freq):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = freq 

class DLL:
    def __init__(self):
        self.head = Node(-1,-1,0)
        self.tail = Node(-1,-1,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def remove_node(self,node):  #the pupose of having -1,-1 at the beginning and the end is to avoid the null error problem
        pre, nxt = node.prev, node.next  
        pre.next, nxt.prev = nxt, pre

    def add_node(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def update(self,node):      #implements the remove and add operations (oh, for get operation)
        self.remove_node(node)
        self.add_node(node)
        node.freq += 1 #freq increases as interactions occur

    def insert(self,node):
        self.add_node(node)
        self.count += 1
        return node #the purpose of returning this is to be able to add it to the hashmap

    def remove_last(self):
        last = self.tail.prev
        self.remove_node(last)
        self.count -= 1
        return last  #the purpose of returning this is to be able to delete it from the hashmap

    def remove_least_freq(self,node):
        #check if there's more than one node with this frequency, consider LRU if there's more
        frequency = node.freq
        subdll = DLL()
        p = subdll.head.next
        while p.next is not subdll.tail:
            if p.freq == frequency: #create a sub-dll
                subdll.insert(p)
            p = p.next 
        if subdll.count == 1:
            self.remove_node(node) #the node could be in the middle
        else:
            #remove last of node with frequency
            last_freq = subdll.remove_last()
            self.remove_node(last_freq)


class LFUCache:
    def __init__(self,capacity):
        self.dll = DLL()
        self.dic = {}
        self.cap = capacity 

    def get(self,key):
        if key in self.dic:
            node = self.dic[key]
            self.dll.update(node)
            return node.val 
        else:
            return -1

    def put(self,key,value):
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.dll.update(node)
        else:
            if self.dll.count == self.cap:
                #get node with minimum freq
                key_min_freq = min(self.dic, key=lambda k: self.dic[k].freq) #might be wrong
                remove_node = self.dic[key_min_freq]
                self.dll.remove_least_freq(remove_node) #calling it last, could be least frequent
                del self.dic[key_min_freq]
            node = Node(key,value,0)
            self.dic[key] = node
            self.dll.insert(node) 

cache = LFUCache(3)
cache.put(1,1)
cache.put(2,2)
cache.put(3,3)
cache.put(4,4)
res = cache.get(1)
print(res)

