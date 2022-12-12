# 백준 24077번 比較 (Comparison)
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = sorted([int(_) for _ in put().split()])
B = sorted([int(_) for _ in put().split()], reverse=True)
cnt = 0

for n in range(N):
    for m in range(M):
        if A[n] <= B[m]:
            cnt += 1
        else:
            break

print(cnt)

