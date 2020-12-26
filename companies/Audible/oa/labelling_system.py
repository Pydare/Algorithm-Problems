from queue import PriorityQueue

def relabel(original_label, k):
    new_label, prev_char = "", ""
    pq = PriorityQueue()

    for i, ch in enumerate(original_label):
        pq.put((-(ord(ch)-ord('a')), i, ch))

    checker = 1
    while not pq.empty():
        pos, i, check_char = pq.get()
        if i != 0:
            if prev_char == check_char:
                checker += 1
                if checker <= k:
                    new_label += check_char
                    prev_char = check_char
                else:
                    temp_pos, j, temp_char = pq.get()
                    if not pq.empty() and prev_char != temp_char:
                        prev_char = temp_char
                        new_label += prev_char
                        pq.put((pos, i, check_char))
                    else:
                        pq.put((temp_pos, j, temp_char))

            else:
                checker = 1
                new_label += check_char
                prev_char = check_char

        else:
            new_label += check_char
            prev_char = check_char

    return new_label

ans = relabel("aabaccc", 2)
print(ans)

############### UNEVEN BUT OPTIONAL CODE ##############################
s = 'baccc' # ccbca
# s = 'aabaccc' # ccbacaa
# s = 'aaabbbcccddd' # => ddcdccbbabaa
# s = 'abbbbbbbc'   # not possible 
# s = 'abbbbbbc' # EDGE CASE IMPORTANT*** => bbcbbabb
# s = 'daabaabc' # => dcbaabaa
# s = 'aaaaabbbbbcccccddddd' # => ddcddcdccbcbbabaabaa
k = 2
s = sorted(s)
length = len(s)
flag = 0
remains = list()
alike = s[-1] 
for i in range(len(s)-1,-1,-1):
    toset = list()
    if s[i] == alike and i == 0 :
        flag+=1
        toset = s[i+k : flag]
        del s[i+k : flag]
    elif s[i] == alike  :
        flag += 1
        continue
    elif s[i] != alike :
        if flag > k :
            j = i
            toset = s[i+1 : i+1+flag-k]
            del s[i+1 : i+1+flag-k]
            while toset and j >= 0 :
                if len(toset)<k :
                    while toset :
                        s.insert(j,toset[0])
                        toset.pop(0)
                else:
                    p = 0
                    while p < k :
                        s.insert(j,toset[0])
                        toset.pop(0)
                        p+=1
                j-=1
        flag = 1
        alike = s[i]
    if toset :
        remains.append(toset)

for i in range(len(remains)):
    j = 0
    while remains[i] and j < len(s)-1 :
        if s[j] != remains[i][0] and s[j+1] != remains[i][0] :
            if len(remains[i]) > k :
                p = 0
                while p < k :
                    s.insert(j+1,remains[i][0])
                    remains[i].pop(0)
                    p+=1
            else :
                while remains[i] :
                    s.insert(j+1,remains[i][0])
                    remains[i].pop(0)
        elif s[j] == remains[i][0] and s[max(0,j-1)] != remains[i][0]:
            if s[j:j+k+1].count(remains[i][0]) < k :
                rem = k - s[j:j+k+1].count(remains[i][0]) 
                while rem and remains[i] :
                    s.insert(j,remains[i][0])
                    remains[i].pop(0)
                    rem-=1 
        elif s[j+1] != remains[i][0] and j+1 == len(s)-1:
            p = 0
            while remains[i] and p < k :
                s.append(remains[i][0])
                remains[i].pop(0)
                p+=1
        j += 1

result = ''.join([i for i in s[::-1]])
print(result)