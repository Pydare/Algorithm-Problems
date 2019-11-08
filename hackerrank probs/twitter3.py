def finalPrice(prices):
    l = []
    for i in range(len(prices)):
        temp = [prices[j] for j in range(i+1,len(prices))]    
        temp.append(0)
        a = prices[i]
        for j in temp:
            if j<=a:
                p = a-j
                break
            else:
                p = a
        l.append(p)
    total = sum(l)
    print(total)
    for i in range(len(prices)):
        if l[i] == prices[i]:
            print(i,end = ' ')


finalPrice([5,1,3,4,6,2])
    
                
    


