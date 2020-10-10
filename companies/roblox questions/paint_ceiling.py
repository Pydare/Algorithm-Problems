import itertools
def variants_count(n,s0,k,b,m,a):
    lengths = get_length(n,s0,k,b,m)
    count = 0

    #checking for the same length and breadth
    for length in lengths:
        if length*length <= a:
            count += 1

    for i,j in itertools.permutations(lengths,2):
        if i*j <= a:
            count += 1
    
    return count

def get_length(n,s0,k,b,m):
    res = [0]*(n+1)
    res[0] = s0
    for i in range(1,n+1):
        res[i] = ((k*res[i-1]+b)%m) + 1 + res[i-1]

    return res

ans = variants_count(3,2,3,3,2,15)
print(ans)
