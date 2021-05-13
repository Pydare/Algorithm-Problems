from collections import defaultdict
def areSentencesSimilarTwo(self, words1, words2, pairs):
        
    if len(words1) != len(words2):
        return False
    
    graph = defaultdict(list)
    for w1, w2 in pairs:
        graph[w1].append(w2)
        graph[w2].append(w1)
        
    print(dict(graph))
        
    def dfs(source, target):
        if source == target:
            return True
        seen.add(source)
        for nei in graph[source]:
            if nei not in seen:
                ret =  dfs(nei, target)
                if ret:
                    return True
        return False
        
    for w1, w2 in zip(words1, words2):
        seen = set()
        if not dfs(w1, w2):
            return False
        
    return True