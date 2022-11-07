# 백준 13772번 Holes
import sys
put = sys.stdin.readline

N = int(put())

while N:
    N -= 1
    s = put().strip().replace(' ', '')
    cnt = 0

    for i in s:
        if i == 'B':
            cnt += 2

        elif i in {'A', 'D', 'O', 'P', 'Q', 'R'}:
            cnt += 1

    print(cnt)