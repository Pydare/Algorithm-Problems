"""
pages = [12,34,67,90]
lo = 12 hi = 203 mid = 107
m = 2
"""
import sys
def minimum_pages(pages,m):
    lo, hi = pages[0], sum(pages)
    res = sys.maxsize
    while lo < hi:
        mid = (lo+hi)//2
        #print(mid)
        if is_possible(pages,mid,m):
            res = min(res,mid)
            hi = mid
        else:
            lo = mid+1
    return res
        
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
            return False #mid is too low
    else:
        return True

####CORRECTION
def find_pages(pages,students):

    n = len(pages)
    summ = sum(pages)

    if n < students:
        return -1

    lo, hi = max(pages), summ
    res = sys.maxsize

    while lo < hi:
        mid = (lo+hi)//2
        if is_possible2(pages,n,students,mid):
            res = min(res,mid)
            hi = mid
        else:
            lo = mid+1

    return res

def is_possible2(pages,n,students,mid): # [12,34,67,90] 113
    students_required = 1
    curr_sum = 0

    for i in range(n):
        # check if current no. of pages > mid, ie mid is too small ---> note that this condition was already checked for in line 44 (lo=max(pages))
        if pages[i] > mid:
            return False
        
        #count how many students are required to distribute the mid pages
        if curr_sum + pages[i] > mid:
            students_required += 1
            curr_sum = pages[i]

            if students_required > students:
                return False
        else:
            curr_sum += pages[i]
    
    return True

ans = find_pages([12,34,67,90],2)
print(ans)
