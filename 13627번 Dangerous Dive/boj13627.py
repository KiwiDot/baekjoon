# 백준 13627번 Dangerous Dive
import sys
put = sys.stdin.readline

N, R = map(int, put().split())
num = set([int(_) for _ in put().split()])

if N == R:
    print('*')

else:
    n = set([i for i in range(1, N+1)])

    for i in sorted(list(n - num)):
        print(i, end=' ')
    print()