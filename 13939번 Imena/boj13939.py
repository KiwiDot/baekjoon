# 백준 13939번 Imena
import sys
put = sys.stdin.readline

N = int(put())
s = put().split()
num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
cnt = 0

for i in s:
    if not set(i) & num and i == i.capitalize():
        cnt += 1

    if i[-1] in {'.', '?', '!'}:
        print(cnt)
        cnt = 0