# 백준 17577번 Scores of Final Examination
import sys
put = sys.stdin.readline

while True:
    n, m = map(int, put().split())
    if n == m == 0:
        break
    s = [0] * n

    while m:
        m -= 1
        p = [int(_) for _ in put().split()]

        for i in range(n):
            s[i] += p[i]

    print(max(s))