# l = range(21,30)
# for i,v in enumerate(l):
#     #print(i+1,v)
#     check = [(v-(i+1)) for i,v in enumerate(l)]
# print(check)

#l = [[5,1],[2,1],[0,1],[1,1],[8,1],[10,0],[5,0]]

########################################################
# for i in l:
#     i[0],i[1] = i[1],i[0]
# k=5
# l.sort()

# new_subtract = []
# for i,v in enumerate(l):
#     if l[i][0]==1 and i<k+1 :
#         new_subtract.append(l[i][1])
    
# print(new_subtract)
# print(l)
#########################################################








l = [[13,1],[10,1],[9,1],[8,1],[13,0],[12,0],[18,1],[13,1]]
#l = [[5,1],[2,1],[0,1],[1,1],[8,1],[10,0],[5,0]]

for i in l:
    i[0],i[1] = i[1],i[0]

l.sort()
#print(l[-4][1])
n = [i[0] for i in l]
k = 5
first = [i[0] for i in l]
new_subtract = []
for i,v in enumerate(l):
    if l[i][0]==1 and i<(len(l)-k) :
        new_subtract.append(l[i][1])
second = [i[1] for i in l[-(k):]]
subtract = l[-3]

zeros_sum = [i[1] for i in l if i[0]==0]
second = second + zeros_sum
print(l)
print(sum(second)-sum(new_subtract))






