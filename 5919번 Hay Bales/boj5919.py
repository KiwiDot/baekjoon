# 백준 5919번 Hay Bales
import sys
put = sys.stdin.readline

N = int(put())
n = [int(put()) for i in range(N)]
avg = sum(n) // N
cnt = 0

for i in n:
    if i > avg:
        cnt += i - avg

print(cnt)