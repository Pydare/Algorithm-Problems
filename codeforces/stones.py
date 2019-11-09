def maxStones(l):
    count = 0
    while True:
        ft_a = l[0] - 1
        ft_b = l[1] - 2

        st_b = l[1] - 1
        st_c = l[2] - 2

        if st_b>ft_b and st_c>2:
            l[1] == st_b
            l[2] = st_c
            count += 3
        elif st_b<ft_b and  :
            l[0] = ft_a
            l[1] = ft_b
            count += 3
        ##terminating condition for the loop
        if l[2] == 0:
            break
        if l[0]<1 and (l[1]<1 or l[2]<2):
            break
        if l[2]<1 and (l[0]<1 or l[1]<2):
            break
    print(count)

maxStones([3,3,0])
        
        