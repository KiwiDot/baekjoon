# 백준 9611번 Vicinity
import sys
put = sys.stdin.readline

n = int(put())
p = [[int(_) for _ in put().split()] for i in range(n)]

t = int(put())
while t:
    t -= 1
    i, d = map(int, put().split())

    x1, y1 = p[i-1]
    cnt = -1

    for j in p:
        x2, y2 = j
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= d ** 2:
            cnt += 1

    print(cnt)