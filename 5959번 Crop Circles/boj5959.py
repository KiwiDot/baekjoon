# 백준 5959번 Crop Circles
import sys
put = sys.stdin.readline

N = int(put())
x, y, r = [], [], []
cnt = [0] * N

for i in range(N):
    X, Y, R = map(int, put().split())
    x.append(X)
    y.append(Y)
    r.append(R)

for i in range(N-1):
    x1, y1, r1 = x[i], y[i], r[i]
    for j in range(i+1, N):
        x2, y2, r2 = x[j], y[j], r[j]

        if (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 + r2) ** 2:
            cnt[i] += 1
            cnt[j] += 1

for i in cnt:
    print(i)