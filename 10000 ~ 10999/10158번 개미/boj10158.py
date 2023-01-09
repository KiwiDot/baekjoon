# 백준 10158번 개미
import sys
put = sys.stdin.readline

w, h = map(int, put().split())
p, q = map(int, put().split())
t = int(put())
drt = {1: [1, 1], 2: [-1, 1], 3: [-1, -1], 4: [1, -1]}
d = 1

while t > 0:
    if d == 1:
        xy = min(t, w - p, h - q)
        p += xy
        q += xy

        if p == w and q == h:
            d = 3
        elif p == w:
            d = 2
        else:
            d = 4

    elif d == 2:
        xy = min(t, p, h - q)
        p -= xy
        q += xy

        if p == 0 and q == h:
            d = 4
        elif p == 0:
            d = 1
        else:
            d = 3

    elif d == 3:
        xy = min(t, p, q)
        p -= xy
        q -= xy

        if p == 0 and q == 0:
            d = 1
        elif p == 0:
            d = 4
        else:
            d = 2

    else:
        xy = min(t, w - p, q)
        p += xy
        q -= xy

        if p == w and q == 0:
            d = 2
        elif p == w:
            d = 3
        else:
            d = 1
    t -= xy

print(p, q)