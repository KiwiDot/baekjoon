# 백준 26575번 Pups
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    d, f, p = map(float, put().split())
    print("${:.2f}".format(d * f * p))