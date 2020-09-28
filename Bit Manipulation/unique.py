#note that this method is used for twice repeated characters only
def non_repeated(arr):
    x = 0
    for num in arr:
        x ^= num
        print(x)
    return x

test = [1,2,1,4,6,2,6]
res = non_repeated([1,1,2,2,3,4,4,4])
#print(res) 