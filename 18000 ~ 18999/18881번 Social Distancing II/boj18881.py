# 백준 18881번 Social Distancing II
import sys
put = sys.stdin.readline

N = int(put())
cow = sorted([[int(_) for _ in put().split()] for i in range(N)])
R = 10 ** 6
cnt = 0

# 감염 범위 구하기
for i in range(N-1):
    x1, s1 = cow[i]
    x2, s2 = cow[i+1]

    # 사회적 거리두기 성공
    if {s1, s2} == {0, 1}:
        R = min(R, abs(x1 - x2))

x = -1
for i in range(N):
    if cow[i][1]:
        if x == -1:
            x = cow[i][0]
            cnt += 1

        elif abs(x - cow[i][0]) < R:
            x = cow[i][0]

        else:
            x = cow[i][0]
            cnt += 1

print(cnt)