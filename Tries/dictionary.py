from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self,word):
        ptr = self.root
        for w in word:
            ptr = ptr.children[w]
        ptr.is_word = True 

    def search(self,word):
        ptr = self.root
        self.res = False
        self.dfs(ptr,word)
        return self.res

    def dfs(self,ptr,word):
        if not word:
            if ptr.is_word:
                self.res = True
            return 
        if word[0] == '.':
            for n in ptr.children.values():
                self.dfs(n, word[1:])
        else:
            ptr = ptr.children.get(word[0])
            if not ptr:
                return
            self.dfs(ptr,word[1:])