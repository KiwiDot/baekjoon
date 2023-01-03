# 백준 13133번 Aurora Princess
import sys
put = sys.stdin.readline

N = int(put())
life = [0] + [1] * N
parent = [[0, 0]] + [[int(_) for _ in put().split()] for i in range(N)]

M = int(put())
m = [int(_) for _ in put().split()] if M else []
cnt = 0

for i in m:
    life[i] ^= 1

for i in range(1, N+1):
    father, mother = parent[i]

    # 자기자신의 생존 여부
    if not life[i]:
        continue    # 사망

    # 부모님의 행방불명 여부
    if not father or not mother:
        continue    # 행방불명

    # 부모님의 생존 여부
    if life[father] and life[mother]:
        cnt += 1    # 생존

print(cnt)