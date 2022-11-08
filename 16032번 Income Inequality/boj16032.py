# 백준 16032번 Income Inequality
import sys
put = sys.stdin.readline

while True:
    n = int(put())
    if not n:
        break
    a = [int(_) for _ in put().split()]

    avg = sum(a) / n
    cnt = 0

    for i in a:
        if i <= avg:
            cnt += 1

    print(cnt)