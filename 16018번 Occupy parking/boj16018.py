# 백준 16018번 Occupy parking
import sys
put = sys.stdin.readline

N = int(put())
yesterday = put().strip()
today = put().strip()
cnt = 0

for i in range(N):
    if yesterday[i] == today[i] == 'C':
        cnt += 1

print(cnt)