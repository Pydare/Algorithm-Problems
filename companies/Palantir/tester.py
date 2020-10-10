def fib_gen(n):
    res = [1]*n
    
    for i in range(2,n):
        res[i] = res[i-1] + res[i-2]
    return res

def findMinFibonacciNumbers(k):
    fib_ref = fib_gen(k)
    count = 0
    starter = len(fib_ref)-1
    
    if max(fib_ref) > k:
        while fib_ref[starter] > k:
            starter -= 1
        if fib_ref[starter] == k:
            count += 1
            return count
        else:
            while k > 0:
                print(starter,k)
                temp = k - fib_ref[starter]
                if temp == 0:
                    count += 1
                    return count
                elif temp in fib_ref:
                    k -= fib_ref[starter]
                    count += 1
                    starter = fib_ref.index(temp)
                else:
                    starter -= 1
    else:
        while k > 0:
            temp = k - fib_ref[starter]
            if temp == 0:
                count += 1
                return count
            elif temp in fib_ref:
                k -= fib_ref[starter]
                count += 1
                starter = fib_ref.index(temp)
            else:
                starter -= 1
                
    return count

ans = findMinFibonacciNumbers(19)
print(ans)