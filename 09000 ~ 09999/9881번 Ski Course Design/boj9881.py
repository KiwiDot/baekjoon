# 백준 9881번 Ski Course Design
import sys
put = sys.stdin.readline

N = int(put())
hill = sorted([int(put()) for i in range(N)])
answer = set()

for i in range(hill[0], hill[N-1]+1):
    minimum, maximum = i, i+17
    cnt = 0

    for j in hill:
        if j < minimum:
            cnt += (minimum - j) ** 2
        elif j > maximum:
            cnt += (j - maximum) ** 2

    answer.add(cnt)

print(min(answer))