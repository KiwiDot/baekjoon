# 백준 24421번 掛け算 (Multiplication)
import sys
put = sys.stdin.readline

N = int(put())
A = [int(_) for _ in put().split()]
cnt = 0

for x in range(N-2):
    for y in range(x+1, N-1):
        for z in range(y+1, N):
            if A[x] * A[y] == A[z]:
                cnt += 1

print(cnt)