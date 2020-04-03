from collections import Counter
def countsentences(wordSet, sentences):
    stringSort = lambda x:''.join(sorted(x))
    sortedWords = [stringSort(word) for word in wordSet]
    wordDic = Counter(sortedWords)
    
    ans = []
    for sentence in sentences:
        sentenceArr = sentence.split(' ')
        count = 1
        for e in sentenceArr:
            count *= wordDic[stringSort(e)] 
        ans.append(count)
        count = 1

    return sentenceArr

words = ["the","bats","tabs","in","cat","act"]
senten = ["cat the bats","in the act", "act tabs in"]
print(countsentences(words, senten))
