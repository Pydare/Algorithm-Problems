"""
pages = [12,34,67,90]
lo = 12 hi = 203 mid = 107
m = 2
"""

def minimum_pages(pages,m):
    lo, hi = pages[0], sum(pages)
    while lo < hi:
        mid = (lo+hi)//2
        #print(mid)
        res =  is_possible(pages,mid,m)
        if res == 0:
            hi = mid
        elif res == 1:
            lo = mid+1
        elif res == 2:
            return mid
        

def is_possible(pages,mid,m):
    i = 0
    students = [0]*m
    for page in pages:
        if students[i] + page >= mid and i != len(students)-1 :
            i += 1
            students[i] += page
        else:
            students[i] += page
    print(students,mid)
    if any(students) > mid:
            return 0 #mid is too low
    elif any(students) < mid:
        return 1 #mid is too high
    elif all(mid) <= mid:
        return 2 #mid is perfect


res = minimum_pages([12,34,67,90], 2)
print(res)
