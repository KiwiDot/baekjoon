# 백준 14409번 Tuna
import sys
put = sys.stdin.readline

N = int(put())
X = int(put())
cnt = 0

while N:
    N -= 1
    P1, P2 = map(int, put().split())

    if abs(P1 - P2) > X:
        P3 = int(put())
        cnt += P3

    else:
        cnt += max(P1, P2)

print(cnt)