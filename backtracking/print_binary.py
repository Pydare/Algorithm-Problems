def binary(digits, prefix):
    #base case
    print(f"Digits is {digits} and Prefix is {prefix}")
    if digits == 0:
        print(prefix)
    else:
        binary(digits-1, prefix+'0')
        binary(digits-1,prefix+'1')

print(binary(3,""))