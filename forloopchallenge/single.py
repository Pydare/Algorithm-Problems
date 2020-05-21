def single2stupor(n):

    def util(n,count):
        if len(str(n)) == 1:
            return count
        else:
            a = 1
            for i in str(n):
                a *= int(i)
            n = a
            return util(n,count+1)
        

    ans = util(n,0)
    return ans

res = single2stupor(42)
print(res)