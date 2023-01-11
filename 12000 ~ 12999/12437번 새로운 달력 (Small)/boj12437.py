# 백준 12437번 새로운 달력 (Small)
import sys
put = sys.stdin.readline

T = int(put())

for t in range(1, T+1):
    m, d, w = map(int, put().split())
    r = 0
    y = 0

    for i in range(1, m+1):
        if r:
            y += 1
            d_ = d + r - w
        else:
            d_ = d

        y += d_ // w
        r = d_ % w
        if r:
            y += 1
    print("Case #{}: {}".format(t, y))