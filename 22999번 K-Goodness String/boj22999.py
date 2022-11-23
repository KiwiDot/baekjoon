# 백준 22999번 K-Goodness String
import sys
put = sys.stdin.readline

T = int(put())

for x in range(1, T+1):
    N, K = map(int, put().split())
    S = put().strip()
    cnt = 0

    for i in range(N//2):
        if S[i] != S[-1-i]:
            cnt += 1

    y = abs(cnt - K)
    print("Case #{}: {}".format(x, y))