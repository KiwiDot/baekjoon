# 백준 9913번 Max
import sys
put = sys.stdin.readline

N = int(put())
num = {}

while N:
    N -= 1
    n = put().strip()
    if n in num:
        num[n] += 1
    else:
        num[n] = 1

print(max(num.values()))