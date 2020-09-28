#returns number of "1" bits
def count_bits(x):
    num_bits = 0
    while x:
        print(x,bin(x),bin(x&1))
        num_bits += x&1
        x >>= 1
    return num_bits

ans = count_bits(20)
print(ans)

for i in range(20):
    print(bin(i))
