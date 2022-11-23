# 백준 9849번 Rect
import sys
put = sys.stdin.readline

n = int(put()) - 1
x1, x2, y1, y2 = map(int, put().split())
check = True

while n:
    n -= 1
    x01, x02, y01, y02 = map(int, put().split())

    if set([i for i in range(x1, x2)]) & set([i for i in range(x01, x02)]) and set([i for i in range(y1, y2)]) & set([i for i in range(y01, y02)]):
        x1, y1 = max(x1, x01), max(y1, y01)
        x2, y2 = min(x2, x02), min(y2, y02)

    else:
        check = False
        break

if check:
    print((x2 - x1) * (y2 - y1))
else:
    print(0)