def findAllConcatenatedWordsInADict(words):
        
    word_set = set(words)
    res = []
    
    
    def is_breakable(word):
        if word == "":
            return True
        
        for i in range(len(word)):
            if word[:i+1] in word_set:
                if is_breakable(word[i+1:]):
                    return True
                
        return False      
    
    for word in words:
        word_set.remove(word)
        if is_breakable(word):
            res.append(word)
        word_set.add(word)
            
    return res

# DISCUSS SOLN BEATS 82%
def findAllConcatenatedWordsInADict2(words):
        
    words = set(words)
    def concat(w):
        for i in range(1, len(w)):
            prefix, suffix = w[:i], w[i:]
            if prefix in words and (suffix in words or concat(suffix)):
                return True
        return False
    return [w for w in words if concat(w)]

# USING MEMOIZATION TO SPEED THINGS UP
def concatenate(words):
    words = set(words)
    memo = {}
    def concat(w):
        if w in memo:
            return memo[w]
        
        memo[w] = False
        for i in range(1, len(w)):
            prefix, suffix = w[:i], w[i:]
            if prefix in words and (suffix in words or concat(suffix)):
                memo[w] =  True
                break
                
        return memo[w]
    
    return [w for w in words if concat(w)]