"""
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
For example, the parity of 1011 is 1, and the parity of 10001000 is 0
"""

def parity_checker(x):
    res = 0
    while x:
        res ^= x&1
        print(res)
        x >>= 1
    return res 

ans = parity_checker(45)
print(ans)


#a more optimized check
def parity_optimized(x):
    res = 0
    while x:
        res ^= 1
        x &= x-1
    return res
    