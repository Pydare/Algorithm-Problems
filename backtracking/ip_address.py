def ip_combinations(s):
    res = []
    sep = '.'
    s = [i for i in s]

    def helper(s,sep):
        #base case  