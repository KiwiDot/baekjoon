# 백준 15234번 Number Pairs
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
num = sorted([int(_) for _ in put().split()])
cnt = 0

for i in range(N-1):
    for j in range(i+1, N):
        if num[i] + num[j] == K:
            cnt += 1

        elif num[i] + num[j] > K:
            break

print(cnt)