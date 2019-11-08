def minimumBribes(q):
    check = [abs(v-(i+1)) for i,v in enumerate(q)]
    g = [] #checking for odd numbers in the check list, which represent 'chaoticness'
    for i in check:
        if (i%2) != 0 and i>2:
            g.append(i) #there has been more than 2 swaps indicating more than 2 bribes
            
    count = (check.count(1))//2
    if check is not None:
        for i in check:
            if i%2 == 0:
                count += (i//2)
        
    if g:
        print('Too chaotic')
    if not g:
        print((count))
    print(check)
    


#minimumBribes([1,2,5,3,7,8,6,4])
minimumBribes([2,1,5,3,4])
