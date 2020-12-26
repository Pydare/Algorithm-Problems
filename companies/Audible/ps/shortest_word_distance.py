# PART I
def shortestDistance(words, word1, word2):
    i1, i2 = -1, -1
    min_distance = len(words)
    
    for i in range(len(words)):
        if words[i] == word1:
            i1 = i
        elif words[i] == word2:
            i2 = i
            
        if i1 != -1 and i2 != -1:
            min_distance = min(min_distance, abs(i1 - i2))
            
    return min_distance

# PART II
from collections import defaultdict
class WordDistance:

    def __init__(self, words):
        self.locations = defaultdict(list)

        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(words):
            self.locations[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")

        # Until the shorter of the two lists is processed
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff

# YPART III
from collections import defaultdict
class Solution2:
    def shortestWordDistance(self, words, word1: str, word2: str) -> int:
        d = defaultdict(list)
        for i, word in enumerate(words):
            d[word].append(i)
            
        min_dis = float('inf')
        if word1 == word2:
            pos = d[word1]
            for i in range(1, len(pos)):
                min_dis = min(min_dis, pos[i] - pos[i-1])
        else:
            pos1, pos2 = d[word1], d[word2]
            l1, l2 = len(pos1), len(pos2)
            i1 = i2 = 0
            while i1 < l1 and i2 < l2:
                min_dis = min(min_dis, abs(pos1[i1] - pos2[i2]))
                if pos1[i1] < pos2[i2]:
                    i1 += 1
                else:
                    i2 += 1
                    
        return min_dis