def fib(n):
    d = {}
    if n not in d.keys():
        d[n] = _fib(n)
    return d[n]
def _fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


######## initial ###########
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)