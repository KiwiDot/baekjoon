# 백준 11007번 Inverse Move-to-Front Transform
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    MFT = "abcdefghijklmnopqrstuvwxyz"
    n = int(put())
    a = [int(_) for _ in put().split()]
    s = ""

    for i in a:
        s += MFT[i]
        MFT = MFT[i] + MFT[:i] + MFT[i+1:]

    print(s)