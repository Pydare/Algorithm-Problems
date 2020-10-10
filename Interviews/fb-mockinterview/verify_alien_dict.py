def is_alien_sorted(words,order):

    order_index = {c:i for i,c in enumerate(order)}

    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]

        #find the first different word word1[k] != word2[k]
        for k in range(min(len(word1), len(word2))):
            #if they compare badly its not sorted
            if word1[k] != word2[k]:
                if order[word1[k]] > order[word2[k]]:
                    return False
                break
            else:
                #if we didnt find a first difference, the words are like app and apple
                if len(word1) > len(word2):
                    return False

    return True


##################################ALIEN DICTIONARY###################
from collections import defaultdict, Counter, deque

def alien_order(words):

    #step 0: create data structures + the indegree of each unique letter to be 0
    adj_list = defaultdict(set)
    indegree = Counter({c:0 for word in words for c in word})

    #step 1: populated adlist and indegree
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]

        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if word2[j] not in adj_list[word1[j]]:
                    adj_list[word1[j]].add(word2[j])
                    indegree[word2[j]] += 1
                break
        else:
            if len(word1) > len(word2):
                return ""

    #step 2: repeatedly pick off nodes with indegree of 0
    output = []
    q = deque([c for c in indegree if indegree[c] == 0])

    while q:
        node = q.popleft()
        output.append(node)
        for nei in adj_list[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    #if not all letters are in output that means there's a cycle and no valid order
    return "" if len(output) < len(indegree) else "".join(output)