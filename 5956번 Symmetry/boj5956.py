# 백준 5956번 Symmetry
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
field = 1
cnt = 0

while N % 2 and M % 2:
    cnt += field

    N //= 2
    M //= 2
    field *= 4

print(cnt)