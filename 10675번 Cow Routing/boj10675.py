# 백준 10675번 Cow Routing
import sys
put = sys.stdin.readline

A, B, N = map(int, put().split())
c = []

while N:
    N -= 1
    cost, city = map(int, put().split())
    cities = [int(_) for _ in put().split()]

    a, b = 0, 0
    if A in cities:
        a = cities.index(A) + 1

    if B in cities:
        b = cities.index(B) + 1

    if (a and b) and (a < b):
        c.append(cost)

if c:
    print(min(c))

else:
    print(-1)