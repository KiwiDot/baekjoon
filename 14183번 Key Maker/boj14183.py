# 백준 14183번 Key Maker
import sys
put = sys.stdin.readline

while True:
    m, n = map(int, put().split())
    if m == n == 0:
        break

    customer = [int(_) for _ in put().split()]
    cnt = 0

    while n:
        n -= 1
        k = [int(_) for _ in put().split()]
        check = True
        for i in range(m):
            if k[i] > customer[i]:
                check = False
                break

        if check:
            cnt += 1

    print(cnt)