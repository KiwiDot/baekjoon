# 백준 6139번 Speed Reading
import sys
put = sys.stdin.readline

N, K = map(int, put().split())

while K:
    K -= 1
    S, T, R = map(int, put().split())
    r = N // (S * T)
    cnt = T * r + R * (r-1)

    if N % (S * T):
        cnt += R + (N % (S * T)) // S + 1 if N % S else R + (N % (S * T)) // S

    print(cnt)