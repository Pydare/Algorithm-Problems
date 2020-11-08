x, reverted = 121, 0
while x > reverted:
    reverted = reverted * 10 + x%10
    x //= 10
    print(reverted)