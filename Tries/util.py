class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def char_to_int(self,s):
        return ord(s) - ord('a')

    def insert(self, string):
        length = len(string)
        ptr = self.root

        for idx in range(len(string)):
            i = self.char_to_int(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                ptr.children[i] = Node()
                ptr = ptr.children[i]
        ptr.is_end = True

    def remove(self,string):
        ptr = self.root
        length = len(string)

        for idx in range(len(string)):
            i = self.char_to_int(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                raise ValueError("Keyword doesn't exist in trie")
        if ptr.is_end is not True:
            raise ValueError("Keyword doesn't exist in trie")
        ptr.is_end = False
        return

    def search(self,string):
        ptr = self.root
        length = len(string)

        for idx in range(len(string)):
            i = self.char_to_int(string[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                return False
        if ptr.is_end is not True:
            return False
        return True

    def get_all(self,ptr,key,key_list):
        if ptr is None:
            key_list.append(key)
            return 
        if ptr.is_end:
            key_list.append(key)
        for i in range(26):
            if ptr.children[i] is not None:
                self.get_all(ptr.children[i], key+chr(ord('a') + i), key_list)

    def search_by_prefix(self,key):
        ptr = self.root
        key_list = []
        length = len(key)

        for idx in range(length):
            i = self.char_to_int(key[idx])
            if ptr.children[i] is not None:
                ptr = ptr.children[i]
            else:
                return None
        self.get_all(ptr,key,key_list)
        return key_list

