# 백준 19939번 박 터뜨리기
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
k = K * (K+1) // 2

if N < k:
    print(-1)

else:
    N -= k
    maximum = K + N // K + 1 if N % K else K + N // K
    minimum = 1 + N // K

    print(maximum - minimum)