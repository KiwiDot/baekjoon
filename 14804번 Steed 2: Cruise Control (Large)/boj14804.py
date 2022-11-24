# 백준 14804번 Steed 2: Cruise Control (Large)
import sys
put = sys.stdin.readline

T = int(put())

for t in range(1, T+1):
    D, N = map(int, put().split())
    horse = []

    while N:
        N -= 1
        K, S = map(int, put().split())
        horse.append((D - K) / S)

    print("Case #{}: {:.6f}".format(t, D / max(horse)))