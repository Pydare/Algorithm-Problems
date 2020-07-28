def count_primes(n):
    if n < 3:
        return 0
    primes = [True]*n
    primes[0] = primes[1] = False

    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            print(f"before: {primes}")
            primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
            print(f"after:   {primes}")
    return sum(primes)

ans = count_primes(10)
print(ans)
