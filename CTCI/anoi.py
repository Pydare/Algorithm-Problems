def towerOfAnoi(s,d,e,n):
    if n <= 0:
        return
    towerOfAnoi(s,d,e,n-1)
    print(f"Move disk {n} from {s} to {d}")
    towerOfAnoi(e,d,s,n-1)


print(towerOfAnoi('s','d','e',4))