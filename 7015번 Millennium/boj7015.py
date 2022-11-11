# 백준 7015번 Millennium
import sys
put = sys.stdin.readline

n = int(put())
millennium = 196471

while n:
    n -= 1
    Y, M, D = map(int, put().split())

    if Y % 3:
        day = 39 * 5 * (Y-1) + 19 * (M-1) + M//2 + D + (Y//3) * 5

    else:
        day = 39 * 5 * (Y-1) + 20 * (M-1) + D + (Y-1)//3 * 5

    print(millennium - day)