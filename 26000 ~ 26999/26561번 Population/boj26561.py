# 백준 26561번 Population
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    p, t = map(int, put().split())

    p += t // 4
    p -= t // 7
    print(p)