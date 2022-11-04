# 백준 8912번 Sales
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    n = int(put())
    A = [int(_) for _ in put().split()]
    B = [0] * n

    for i in range(1, n):
        for j in range(i):
            if A[i] >= A[j]:
                B[i] += 1

    print(sum(B))