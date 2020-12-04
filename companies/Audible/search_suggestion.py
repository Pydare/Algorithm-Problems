class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, string):
        ptr = self.root
        n = len(string)
        for i in range(n):
            ch = string[i]
            idx = ord(ch) - ord("a")
            if ptr.children[idx] is not None:
                ptr = ptr.children[idx]
            else:
                ptr.children[idx] = Node()
                ptr = ptr.children[idx]
        ptr.is_end = True
        
    def search_by_prefix(self, key):
        ptr = self.root
        key_list = []
        n = len(key)
        for i in range(n):
            ch = key[i]
            idx = ord(ch) - ord("a")
            if ptr.children[idx] is not None:
                ptr = ptr.children[idx]
            else:
                return []
        self.get_all(ptr, key, key_list)
        return key_list
    
    def get_all(self, ptr, key, key_list):
        if len(key_list) == 3:
            return
        if ptr is None:
            key_list.append(key)
            return
        if ptr.is_end:
            key_list.append(key)
        
        for i in range(26):
            if ptr.children[i] is not None:
                self.get_all(ptr.children[i], key + chr(ord("a")+i), key_list)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie_node = Trie()
        output = []
        for product in products:
            trie_node.insert(product)
            
        temp_search = ""
        for ch in searchWord:
            temp_search += ch
            res = trie_node.search_by_prefix(temp_search)
            output.append(res)
            
        return output