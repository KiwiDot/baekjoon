# 백준 9196번 정수 직사각형
import sys
put = sys.stdin.readline

while True:
    h, w = map(int, put().split())
    if h == w == 0:
        break

    d = h ** 2 + w ** 2
    check = False

    while True:
        for x in range(1, int(d ** 0.5) + 1):
            y = (d - x ** 2) ** 0.5
            if y.is_integer() and y > x:
                if d > h ** 2 + w ** 2 or x > h:
                    y = int(y)
                    print(x, y)
                    check = True
                    break

        d += 1
        if check:
            break
