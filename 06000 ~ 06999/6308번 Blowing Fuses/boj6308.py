# 백준 6308번 Blowing Fuses
import sys
put = sys.stdin.readline
t = 0

while True:
    t += 1
    n, m, c = map(int, put().split())
    if n == m == c == 0:
        break

    ci = [0] + [int(put()) for i in range(n)]
    ni = [0] * (n+1)
    check = True
    maximum = 0
    fuse = 0

    while m:
        m -= 1
        num = int(put())
        ni[num] ^= 1

        if ni[num]:
            fuse += ci[num]
        else:
            fuse -= ci[num]

        maximum = max(maximum, fuse)
        if fuse > c:
            check = False

    print("Sequence {}".format(t))
    if check:
        print("Fuse was not blown.")
        print("Maximal power consumption was {} amperes.".format(maximum))
    else:
        print("Fuse was blown.")
    print()