# 백준 26332번 Buying in Bulk
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    c, p = map(int, put().split())
    print(c, p)
    print(p + (c - 1) * (p - 2))