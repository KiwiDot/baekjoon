# 백준 26145번 출제비 재분배
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
S = [int(_) for _ in put().split()] + [0] * M

for i in range(N):
    T = [int(_) for _ in put().split()]
    S[i] -= sum(T)

    for j in range(N+M):
        S[j] += T[j]

print(' '.join([str(_) for _ in S]))