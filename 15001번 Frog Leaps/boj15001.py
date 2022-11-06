# 백준 15001번 Frog Leaps
import sys
put = sys.stdin.readline

n = int(put()) - 1
x0 = int(put())
cnt = 0

while n:
    n -= 1
    x = int(put())
    cnt += (x - x0) ** 2
    x0 = x

print(cnt)