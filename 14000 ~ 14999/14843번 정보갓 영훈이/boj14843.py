# 백준 14843번 정보갓 영훈이
import sys
put = sys.stdin.readline

N = int(put())
score = 0
others = []

while N:
    N -= 1
    S, A, T, M = map(float, put().split())
    score += S * (1 + 1/A) * (1 + M/T) / 4
others.append(score)

P = int(put())
for p in range(P):
    R = float(put())
    others.append(R)

others.sort(reverse=True)
ranking = (others.index(score) + 1)
p = (P+1) * 0.15

if ranking <= p:
    he = "Younghoon \"The God\""
else:
    he = "Younghoon"

print("The total score of {} is {:.2f}.".format(he, score))