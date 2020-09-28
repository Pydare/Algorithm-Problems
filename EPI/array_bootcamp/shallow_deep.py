##shallow copying
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) #we can also use copy.copy()

#wont change ys
xs.append(['new sublist'])

#would change xs due to the reference feature
xs[0][1] = 'X'



#DEEP COPYING
import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)

#won't change zs
xs[1][0] = 'X'

###common methods
"""
A = [1,2,3]
A.reverse() -> (in-place)
reversed(A) -> (retums an iterator)
A.sort() -> (in-place) 
sorted(A) -> (retums a copy)
"""