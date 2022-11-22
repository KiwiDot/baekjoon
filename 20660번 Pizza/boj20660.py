# 백준 20660번 Pizza
import sys
put = sys.stdin.readline

a = set(put().split()[1:])
m = int(put())
cnt = 0

while m:
    m -= 1
    b = set(put().split()[1:])
    if not a & b:
        cnt += 1

print(cnt)