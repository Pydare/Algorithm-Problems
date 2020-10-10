###### time: O(nlogn)  space: O(n)

from collections import OrderedDict
def num_players(k,n,scores):
    scores.sort(reverse=True)
    d = OrderedDict()
    count = i = 0

    for score in scores:
        if score not in d:
            d[score] = 1
        else:
            d[score] += 1

    for key,val in d.items():
        if key == 0:
            continue
        count += val
        i += 1

        if i == k:
            break
    return count

res = num_players(4,5,[2,2,3,4,5])
print(res)


### *assuming its sorted time: O(n)  space: O(1)
def num_players2(k,n,scores):
    k_count = total = i = 1
    scores.reverse()

    while i < len(scores):
        if scores[i] == 0:
            i += 1
            continue
        if scores[i] != scores[i-1]:
            k_count += 1
            total += 1
            while i+1 < len(scores) and scores[i+1] == scores[i]:
                i += 1
                total += 1
        if k_count == k:
            break
        i += 1

    return total

res2 = num_players2(4,5,[100,50,50,25])
print(res2)