def merge_sort(a):
    n = len(a)
    temp = [None]*n
    size = 1
    while size <= n-1:
        sort_pass(a,temp,size,n)
        size = size*2

def sort_pass(a,temp,size,n):
    low1 = 0
    while low1+size < n-1:
        up1 = low1 + size-1
        low2 = low1 + size
        up2 = low2 + size-1

        if up2 >= n: # if length of last sublist is less than size
            up2 = n-1
        merge(a,temp,low1,up1,low2,up2)
        low1 = up2 + 1 #take next two sublists for merging

    for i in range(low1,n):
        temp[i] = a[i]

    copy(a,temp, n)

def merge(a,temp,low1,up1,low2,up2):
    i = low1
    j = low2
    k = low1

    while i <= up1 and j <= up2:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i+=1
        else:
            temp[k] = a[j]
            j+=1
        k+=1
    while i <= up1:
        temp[k] = a[i]
        i+=1
        k+=1
    while j <= up2:
        temp[k] = a[j]
        j+=1
        k+=1

 
def copy(a,temp,n):
    for i in range(n):
        a[i] = temp[i]

list1 = [6,3,1,5,9,8]
merge_sort(list1)
print(list1)