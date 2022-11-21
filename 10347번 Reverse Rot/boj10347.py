# 백준 10347번 Reverse Rot
import sys
put = sys.stdin.readline
apb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    N = put().split()
    if N == ['0']:
        break

    n = int(N[0])
    S = ""
    for i in N[1]:
        S += apb[apb.index(i) + n]

    print(S[::-1])