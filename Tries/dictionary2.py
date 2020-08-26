class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self,word):
        ptr = self.root
        for symbol in word:
            ptr = ptr.children.setdefault(symbol,TrieNode())
        ptr.end_node = True

    def delete(self,word):
        ptr = self.root
        for symbol in word:
            if symbol not in ptr.children:
                raise ValueError("word doesn't exist")
            ptr = ptr.children[symbol]
        if ptr.end_node is not True:
            raise ValueError("word doesn't exist")
        ptr.end_node = False
        return 

    def search(self,word):

        def dfs(ptr,i):
            if i == len(word):
                return ptr.end_node
            if word[i] == '.':
                for child in ptr.children:
                    if dfs(ptr.children[child], i+1):
                        return True

            if word[i] in ptr.children:
                return dfs(ptr.children[word[i]], i+1)

            return False

        return dfs(self.root,0)

    def search_by_prefix(self,key):
        ptr = self.root
        key_list = []

        for symbol in key:
            if ptr.children.get(symbol,None) is not None:
                ptr = ptr.children[symbol]
            else:
                return None
        self.get_all(ptr,key,key_list)
        return key_list

    def get_all(self,ptr,key,key_list):
        if ptr is None:
            key_list.append(key)
            return
        if ptr.end_node:
            key_list.append(key)
        for child in ptr.children:
            if ptr.children[child] is not None:
                self.get_all(ptr.children[child], key+child, key_list)



wd = WordDictionary()
wd.add_word("ad")
wd.add_word("addernt")
wd.add_word("addition")
wd.add_word("adjective")
wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")
wd.delete("mad")
res = wd.search_by_prefix("x")
print(res) 
# wd.search("bad") 
# wd.search(".ad") 
# wd.search("b..") 