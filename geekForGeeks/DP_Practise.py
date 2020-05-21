def isSubSetSum(set_,n,sum_):
    #base case
    if sum_ == 0:
        return True
    if (n==0 and sum_!=0):
        return False
    
    #if last element is greater than sum, then ignore it
    if (set_[n-1] > sum_):
        return isSubSetSum(set_,n-1,sum_)
    else:
        return isSubSetSum(set_,n-1,sum_) or isSubSetSum(set_,n-1,sum-set_[n-1]