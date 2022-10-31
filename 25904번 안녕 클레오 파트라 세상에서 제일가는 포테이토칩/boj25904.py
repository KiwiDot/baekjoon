# 백준 25904번 안녕 클레오 파트라 세상에서 제일가는 포테이토칩
import sys
put = sys.stdin.readline

N, X = map(int, put().split())
T = [int(_) for _ in put().split()]
t = {}

for i in range(N):
    n = -1 if T[i] < X + i else T[i] - X - i
    if n == - 1:
        t[i+1] = -1
    else:
        t[i+1] = n // N + 1

print(min(t, key=t.get))
