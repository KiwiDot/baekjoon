# 백준 5462번 POI
import sys
put = sys.stdin.readline

N, T, P = map(int, put().split())   # 필립의 ID는 P
score = [0] * T  # 각 문제 별 점수
solve = [[int(_) for _ in put().split()] for i in range(N)]
ranking = [0] * N

for i in range(N):
    for j in range(T):
        if not solve[i][j]:
            score[j] += 1

for i in range(N):
    s = 0
    for j in range(T):
        s += solve[i][j] * score[j]

    ranking[i] = s * 100000000 + sum(solve[i]) * 10000 + (N - i)
    if i == P - 1:
        p = s

print(p, sorted(ranking, reverse=True).index(ranking[P-1]) + 1)