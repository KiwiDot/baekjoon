# 백준 14542번 Outer Triangle Sum
import sys
put = sys.stdin.readline
idx = 0

while True:
    n = int(put())
    if not n:
        break

    idx += 1
    cnt = int(put())
    n -= 1

    while n:
        n -= 1
        num = [int(_) for _ in put().split()]
        if n:
            cnt += num[0] + num[-1]
        else:
            cnt += sum(num)

    print("Case #{}:{}".format(idx, cnt))