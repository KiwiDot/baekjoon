# 백준 18154번 Speeding
import sys
put = sys.stdin.readline

N = int(put()) - 1
T, D = map(int, put().split())
spd = 0

while N:
    N -= 1
    t, d = map(int, put().split())
    T = t - T
    D = d - D

    spd = max(spd, D // T)
    T, D = t, d

print(spd)