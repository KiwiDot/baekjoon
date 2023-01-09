# 백준 2670번 연속부분최대곱
import sys
put = sys.stdin.readline

N = int(put())
n = [float(put()) for i in range(N)]
dp = [n[0]] + [0] * (N-1)

for i in range(1, N):
    dp[i] = max(n[i], dp[i-1] * n[i])

print("{:.3f}".format(max(dp)))