def leftRotate(n,d):
    count = 0
    while count < d:
        p = n[0]
        n.pop(0)
        n.append(p)

        count += 1
    print(n)


leftRotate([1,2,3,4,5],4)