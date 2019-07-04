# from functools import reduce
# def digit_to_num(digits):
#     return reduce(lambda x,y:x*10+y,digits)

# x = int(digit_to_num([3,5,4,7]))
# print(x)
# x 
def count_match_index(L):
    print(len([num for i,num in enumerate(L) if num == i]))

count_match_index([0,2,2,1,5,5,6,10])