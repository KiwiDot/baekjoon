# 벡준 5489번 Numbers
import sys
put = sys.stdin.readline

N = int(put())
num = {}

while N:
    N -= 1
    n = int(put())

    if n in num:
        num[n] += 1
    else:
        num[n] = 1

maximum = max(num.values())
for i in sorted(num.keys()):
    if num[i] == maximum:
        print(i)
        break