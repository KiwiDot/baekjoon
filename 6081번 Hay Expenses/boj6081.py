# 백준 6081번 Hay Expenses
import sys
put = sys.stdin.readline

N, Q = map(int, put().split())
H = [int(put()) for i in range(N)]

while Q:
    Q -= 1
    S, E = map(int, put().split())

    print(sum(H[S-1:E]))