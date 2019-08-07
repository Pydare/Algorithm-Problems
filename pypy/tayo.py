def lastStoneWeight(l):
    while len(l) > 1:
        if len(l) == 0:
            print(None)
        l.sort()
        if l[-1] == l[-2]:
            l.pop(l[-1])
            l.pop(l[-2])
        elif l[-1] != l[-2]:
            l[-2] = l[-1] - l[-2]
            l.pop(-1)
    print(l)

lastStoneWeight([2,7,4,1,8,1])
# 1 1 2 4 7 
# l = [23,12,56,32,10,5,43]
# x,y = 0,0
# n = []
# for i in l:
#     if(i>y):
#         x=i
#     else:
#         x=y
#     y=x 
#     n.append(y) 
#     l.sort()  
# print (l[len(l)-1],l[len(l)-2])
