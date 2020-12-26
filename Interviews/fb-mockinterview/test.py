from collections import Counter
def mostCommonWord(paragraph: str, banned):
    
    paragraph = map(lambda x:x.lower(), paragraph.split(" ")) 
    count = Counter(paragraph)
    banned = set(banned)
    print(count)
    
    max_val, ans = 0, ""
    for k, v in count.items():
        if v > max_val:
            if k not in banned:
                ans = k
                max_val = v
                
    return ans

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
ans = mostCommonWord(paragraph, banned)
print(ans)