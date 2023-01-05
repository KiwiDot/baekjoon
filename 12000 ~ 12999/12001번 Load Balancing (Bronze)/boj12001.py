# 백준 12001번 Load Balancing (Bronze)
import sys
put = sys.stdin.readline

N, B = map(int, put().split())
cow = []
for i in range(N):
    x, y = map(int, put().split())
    cow.append([x, y])
answer = 1000

for n0 in range(N):
    for n1 in range(N):
        a = cow[n0][0] + 1
        b = cow[n1][1] + 1

        cnt = [0, 0, 0, 0]
        for i in range(N):
            x, y = cow[i]
            if x > a:
                if y > b:
                    cnt[0] += 1
                else:
                    cnt[1] += 1
            else:
                if y > b:
                    cnt[2] += 1
                else:
                    cnt[3] += 1
        answer = min(answer, max(cnt))

print(answer)