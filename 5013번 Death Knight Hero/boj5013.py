# 백준 5013번 Death Knight Hero
import sys
put = sys.stdin.readline

n = int(put())
cnt = 0

while n:
    n -= 1
    k = put().strip()
    if "CD" not in k:
        cnt += 1

print(cnt)