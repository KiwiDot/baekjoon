# 백준 15494번 Davor
import sys
put = sys.stdin.readline

N = int(put())
n = N // 52 // 7

for i in range(1, n):
    X = n - i * 3
    K = i
    if 0 < X <= 100:
        print(X)
        print(K)
        break
