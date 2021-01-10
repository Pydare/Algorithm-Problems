def is_pangram(string):
    seen = [0] * 26

    for ch in string:
        if ch.isalpha():
            seen[ord(ch) - ord("a")] = 1

    return all(i == 1 for i in seen)



# variation problem, k replaceabele (only considering lower case alphabets)
def is_pangram_with_k(S, k):
    """
    aabbcdefghijklmnopqrstuvwx
    [2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
    """
    if len(S) < 26:
        return False
        
    alphabets = [0] * 26
    
    for ch in S:
        alphabets[ord(ch) - ord("a")] += 1
        
    missing = sum(i == 0 for i in alphabets)
    
    return missing <= k