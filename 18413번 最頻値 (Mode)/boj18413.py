# 백준 18413번 最頻値 (Mode)
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
A = [int(_) for _ in put().split()]
B = {}

for i in A:
    if i in B:
        B[i] += 1
    else:
        B[i] = 1

print(max(B.values()))