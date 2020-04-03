def heap_sort(a,n):
    build_heap_bottom_up(a,n)

    while n > 1:
        maxValue = a[1]
        a[1] = a[n]
        a[n] = maxValue
        n -= 1
        restore_down(1,a,n)

def build_heap_bottom_up(a,n):
    i = n//2
    while i >= 1:
        restore_down(i,a,n)
        i -= 1

def restore_down(i,a,n):
    k = a[i]
    l = 2*i
    r = l+1

    while r <= n:
        if k >= a[l] and k >= a[r]:
            a[i] = k
            return
        elif a[l] > a[r]:
            a[i] = a[l]
            i = l
        else:
            a[i] = a[r]
            i = r
        l = 2*i
        r = l+1
    #if the number of nodes is even
    if l ==n and k < a[l]:
        a[i] = a[l]
        i = l
    a[i] = k