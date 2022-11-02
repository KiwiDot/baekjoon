# 백준 25558번 내비게이션
import sys
put = sys.stdin.readline

N = int(put())
sx, sy, ex, ey = map(int, put().split())
navi = {}

for n in range(1, N+1):
    M = int(put())
    x, y = sx, sy
    cnt = 0

    while M:
        M -= 1
        x_, y_ = map(int, put().split())
        cnt += abs(x - x_) + abs(y - y_)
        x, y = x_, y_
    cnt += abs(x - ex) + abs(y - ey)

    navi[n] = cnt

print(min(navi, key=navi.get))