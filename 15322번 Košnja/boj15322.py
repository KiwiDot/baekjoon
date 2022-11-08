# 백준 15322번 Košnja
import sys
put = sys.stdin.readline

K = int(put())

while K:
    K -= 1
    N, M = map(int, put().split())

    r = (min(N, M) - 1) * 2

    print(r)