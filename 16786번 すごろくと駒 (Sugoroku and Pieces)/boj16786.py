# 백준 16786번 すごろくと駒 (Sugoroku and Pieces)
import sys
put = sys.stdin.readline

N = int(put())
X = [int(_) for _ in put().split()]
M = int(put())
A = [int(_) for _ in put().split()]

for a in A:
    if X[a-1] + 1 not in X and X[a-1] < 2019:
        X[a-1] += 1

for i in X:
    print(i)