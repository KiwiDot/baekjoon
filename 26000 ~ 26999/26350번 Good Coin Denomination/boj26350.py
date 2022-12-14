# 백준 26350번 Good Coin Denomination
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    v = put().split()

    print("Denominations: {}".format(' '.join(v[1:])))
    check = True
    d = int(v.pop(0))
    v = sorted([int(_) for _ in v])

    for i in range(d-1):
        if v[i] * 2 > v[i+1]:
            check = False
            break

    if check:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()