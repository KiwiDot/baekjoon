# 백준 15905번 스텔라(STELLA)가 치킨을 선물했어요
import sys
put = sys.stdin.readline

N = int(put())
n = sorted([[int(_) for _ in put().split()] for i in range(N)], reverse=True)
n5 = n[4][0]
cnt = 0

for i in n[5:]:
    if i[0] == n5:
        cnt += 1
    else:
        break

print(cnt)