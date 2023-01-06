# 백준 14721번 성적표
import sys
put = sys.stdin.readline

N = int(put())
xy = [[int(_) for _ in put().split()] for i in range(N)]
RSS = {}

for a in range(1, 101):
    for b in range(1, 101):
        rss = 0
        for i in xy:
            x, y = i
            rss += (y - a * x - b) ** 2

        RSS[rss] = str(a) + ' ' + str(b)

print(RSS[min(RSS.keys())])