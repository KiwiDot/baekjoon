# 백준 9313번 Integer Flipping
import sys
put = sys.stdin.readline

while True:
    A = int(put())
    if A == -1:
        break

    print(int(bin(A)[2:].zfill(32)[::-1], 2))