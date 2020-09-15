import itertools as it

def naive_grouper(inputs,n):
    num_groups = len(inputs)//n #10/2=5
    return [ tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups) ]


def better_grouper(inputs,n):
    iters = [iter(inputs)] * n
    return zip(*iters)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = naive_grouper(nums,2)
print(ans)


########################
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)] 
  
# Key function 
key_func = lambda x: x[0] 
  
for key, group in it.groupby(L, key_func): 
    print(key + " :", list(group))

##########################RLE
s = "aaabbbcccdddssaaa"
zipper = zip(*[ (k,len(list(grp))) for k,grp in it.groupby(s)])
print(list(zipper))
