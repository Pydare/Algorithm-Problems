"""
to multiply x and y we initialize the result to 0 and iterate through the bits
of x, adding 2^k*y to the result if the kth bit of r is 1.
"""
def multiply(x,y):

    def add(a,b):
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b

        while temp_a or temp_b:
            ak,bk = a&k, b&k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin,k,temp_a,temp_b = (carryout << 1, k<<1, temp_a >> 1, temp_b >> 1)
        return running_sum | carryin

        #would be back LOL


##compute x^y
def power(x,y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0/x
    
    while power:
        if power & 1:
            result *= x
        x, power = x*x, power >> 1
    return result

#Reverse digits
def reverse(x):
    res, x_rem = 0, abs(x)
    while x_rem:
        res = res*10 + x_rem%10
        x_rem //= 10
    return -res if x<0 else res

#decimer integer is a palindrome
"""
the number of digits, n, in the input's string rep. is the
log(base 10) of the input value x. n = logx + 1.
msd -> x//10^(n-1)
"""
import math
def is_palindrome_number(x):
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits-1)
    for _ in range(num_digits//2):
        if (x//msd_mask) != (x % 10):
            return False
        x %= msd_mask #remove the most significant digit of x
        x //= 10 #remove the least significant digit of x
        msd_mask //= 10
    return True