# 백준 1002번 터렛
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    x1, y1, r1, x2, y2, r2 = map(int, put().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # 두 원이 일치
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    # 동심원
    elif d == 0:
        print(0)

    # 두 점에서 만난다
    elif (r1 - r2) ** 2 < d < (r1 + r2) ** 2:
        print(2)

    # 두 원이 외접 / 내접
    elif (r1 + r2) ** 2 == d or (r1 - r2) ** 2 == d:
        print(1)

    # 다른 원의 외부 / 내부
    else:
        print(0)