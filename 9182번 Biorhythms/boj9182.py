# 백준 9182번 Biorhythms
import sys
put = sys.stdin.readline
x = 0

while True:
    x += 1
    p, e, i, d = map(int, put().split())
    if p == e == i == d == -1:
        break

    for y in range(d+1, 21253):
        cycles_p = (y-p) % 23 if y >= p else True
        cycles_e = (y-e) % 28 if y >= e else True
        cycles_i = (y-i) % 33 if y >= i else True

        if not cycles_p and not cycles_e and not cycles_i:
            y -= d
            print("Case {}: the next triple peak occurs in {} days.".format(x, y))
            break