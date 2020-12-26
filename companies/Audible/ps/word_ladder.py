from collections import deque, defaultdict

def ladderLength(beginWord: str, endWord: str, wordList) -> int:
    word_set = set(wordList)
    queue = deque([[beginWord, 1]])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append([next_word, length + 1])
    return 0


# PART 2
def findLadders(beginWord: str, endWord: str, wordList):
        
    word_set = set(wordList) # faster checks against dictionary
    layer = {}
    layer[beginWord] = [[beginWord]]  # stores current word and all possible sequences how we got to it
    
    while layer:
        new_layer = defaultdict(list)  # returns [] on missing keys, just to simplify code
        for word in layer:
            if word == endWord:
                return layer[word]
            else:
                for i in range(len(word)):  # change every possible letter and check if it's in dictionary
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word in word_set:
                            new_layer[new_word] += [j + [new_word] for j in layer[word]]
                            print(dict(new_layer))
                            #print(dict(layer))
                            
        word_set -= set(new_layer.keys())  # remove from dictionary to prevent loops
        layer = new_layer # move down to new layer
        
    return []

ans = findLadders('hit', 'cog',["hot","dot","dog","lot","log","cog"])
print(ans)