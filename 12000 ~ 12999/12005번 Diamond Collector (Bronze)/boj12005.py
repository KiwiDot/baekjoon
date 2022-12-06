# 백준 12005번 Diamond Collector (Bronze)
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
diamond = sorted([int(put()) for i in range(N)])
answer = []

for i in range(N):
    cnt = 1
    for j in range(i+1, N):
        if diamond[j] - diamond[i] > K:
            break
        cnt += 1

    answer.append(cnt)
print(max(answer))