# 백준 9947번 Coin tossing
import sys
put = sys.stdin.readline

while True:
    n1, n2 = put().split()
    if n1 == n2 == '#':
        break

    n = int(put())
    cnt1, cnt2 = 0, 0

    while n:
        n -= 1
        s1, s2 = put().split()
        if s1 == s2:
            cnt1 += 1
        else:
            cnt2 += 1

    print(n1, cnt1, n2, cnt2)