def string_permutation(a,l,r):
    if l == r:
        print(''.join(a))

    else:
        a = [i for i in a]
        for i in range(l,r):
            a[l], a[i] = a[i], a[l]
            string_permutation(a,l+1,r)
            a[l], a[i] = a[i], a[l] #backtrack

print(string_permutation('ABC',0,3))
