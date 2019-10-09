def findMedianSortedArray(nums1,nums2):
    d = {}
    l = []
    for i in nums1:
        d[i] = 1
    for i in nums2:
        d[i] = 1
    for key,_ in d.items():
        l.append(key)
        l.sort()
    if len(l) % 2 != 0:
        print(l[len(l)//2])
    else:
        k = len(l)// 2
        print((l[k]+l[k-1])/2)

findMedianSortedArray([1,1],[1,2])