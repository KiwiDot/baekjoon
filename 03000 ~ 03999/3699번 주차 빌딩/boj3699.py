# 백준 3699번 주차 빌딩
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    h, l = map(int, put().split())
    cnt = 0
    car = [0] * h
    maximum = 0

    for i in range(h):
        data = [int(_) for _ in put().split()]
        maximum = max(maximum, max(data))
        car[i] = data

    num = [[0, 0] for i in range(maximum)]
    x = [0] * h

    for i in range(h):
        for j in range(l):
            r = car[i][j]
            if r == -1:
                continue

            num[r-1] = [i, j]

    for i in num:
        xi = abs(x[i[0]] - i[1])
        cnt += i[0] * 20 + min(xi, l-xi) * 5
        x[i[0]] = i[1]

    print(cnt)