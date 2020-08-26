"""
pages = [12, 34, 67, 90]
m = 2, 3,5, whatever 
"""

def min_pages(pages,students):
    res = 0

    students_list = [0] * students

    i = j = 0
    while i < len(pages):
        while j < students:
            students_list[j] = pages[j]
            j += 1
            i = j
        students_list[i%j] += pages[i]
        i += 1

    return students_list

res = min_pages([12,34,67,90], 2)
print(res)