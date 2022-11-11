# 백준 11680번 Dice Cup
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
result = {}
answer = []

for n in range(1, N+1):
    for m in range(1, M+1):
        if n+m in result:
            result[n+m] += 1
        else:
            result[n+m] = 1

max_dice = max(result.values())
for i in sorted(result.keys()):
    if result[i] == max_dice:
        print(i)