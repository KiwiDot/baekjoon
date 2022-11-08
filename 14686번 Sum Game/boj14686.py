# 백준 14686번 Sum Game
import sys
put = sys.stdin.readline

N = int(put())
score1 = [int(_) for _ in put().split()]
score2 = [int(_) for _ in put().split()]
swi, sem = 0, 0
K = 0

for i in range(N):
    swi += score1[i]
    sem += score2[i]

    if swi == sem:
        K = i+1

print(K)