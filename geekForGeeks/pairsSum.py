def findPairs(arr,n):
    d = {}
    for i in range(n-1):
        for j in range(i+1,n):
            s = arr[i] + arr[j]
            if s == d.keys() and s is not None:
                p = d.get(sum)
                print('The two values are ', str(p),' and ',(arr[i],arr[j]))
                break
                
            else:
                d[sum] = (arr[i],arr[j])
        


findPairs([3,4,7,1,2,9,8],7)