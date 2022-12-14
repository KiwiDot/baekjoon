# 백준 26340번 Fold the Paper Nicely
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    v = put().strip()
    print("Data set: {}".format(v))

    garo, sero, fold = map(int, v.split())

    while fold:
        fold -= 1
        if garo > sero:
            garo //= 2
        else:
            sero //= 2

    if garo > sero:
        print(garo, sero)
    else:
        print(sero, garo)
    print()