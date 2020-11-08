class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit


def schedule(job):

    # sort jobs according to finish time
    job = sorted(job, key=lambda x: x.finish)

    # create an array to store solutions of subproblems
    # table[i] stores the profit for jobs till arr[i] (including arr[i])
    n = len(job)
    table = [0] * n

    table[0] = job[0].profit

    #fill entriesin table using recursive property
    for i in range(1, n):
        
        #find profit including the current job
        include_profit = job[i].profit
        l = binary_search(job,i)
        if l != -1:
            include_profit += table[l]

        # store maximum of including and excluding
        table[i] = max(include_profit, table[i-1])

    return table[n-1]

def binary_search(job, start_idx):

    #initialize lo and hi
    lo, hi = 0, start_idx - 1

    # perform bs iteratively
    while lo < hi:
        mid = (lo + hi)//2
        if job[mid].finish <= job[start_idx].start:
            if job[mid+1].finish <= job[start_idx].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid
    
    return -1

"""
(1,2,50) (3,5,20), (6,19,100) (2,100,200)
"""