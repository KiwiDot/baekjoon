# 백준 14551번 Card Game Contest
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
a = 1

while N:
    N -= 1
    A = int(put())
    if A:
        a = a * A % M

print(a % M)