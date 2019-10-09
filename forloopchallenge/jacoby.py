# def trap(height):     
#     def iterate(height, stack):
#         ans = high = 0
#         for h in height:
#             if h >= high:
#                 while stack:
#                     ans += (high - stack.pop())
#                 high = h
#             stack.append(h)
#         return ans
#     stack = []
#     print(iterate(height, stack) + (iterate(stack[::-1], [])))

# trap([0,1,0,2,1,0,1,3,2,1,2,1])


a = ['a','b','c']
b = ['d','e','f']
c = (zip(a,b))
print(list(c))