
'''
AB AC AD BA BC BD CA CB CD DA DB DC ----> Permutation (the order doesn't matter)

AB AC AD BC BD CD -------> Combination (the order matters)

'''

p = [[1,3],[3,0,1],[2],[0]]
for i in range(len(p)):
    for j in range(len(p[i])):
        print(p[i][j])