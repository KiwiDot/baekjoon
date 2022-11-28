# 백준 26026번 Coffee Cup Combo
import sys
put = sys.stdin.readline

n = int(put())
s = put().strip()
cnt = coffee = 0

for i in s:
    if i == '1':
        cnt += 1
        coffee = 2
    else:
        if coffee:
            cnt += 1
            coffee -= 1

print(cnt)