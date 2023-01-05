# 백준 6212번 Dream Counting
import sys
put = sys.stdin.readline

M, N = map(int, put().split())
num = [0] * 10

for i in range(M, N+1):
    for j in str(i):
        num[int(j)] += 1

print(' '.join([str(i) for i in num]))