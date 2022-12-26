# 백준 26509번 Triangle
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    tri1 = sorted([int(_) for _ in put().split()])
    tri2 = sorted([int(_) for _ in put().split()])

    if tri1 == tri2 and tri1[0] ** 2 + tri1[1] ** 2 == tri1[2] ** 2:
        print("YES")
    else:
        print("NO")