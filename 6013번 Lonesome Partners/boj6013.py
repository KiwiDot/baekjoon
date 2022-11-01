# 백준 6013번 Lonesome Partners
import sys
put = sys.stdin.readline

N = int(put())
cow = [[int(_) for _ in put().split()] for i in range(N)]
distance = {}

for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = cow[i]
        x2, y2 = cow[j]

        distance[str(i+1) + " " + str(j+1)] = (x1 - x2) ** 2 + (y1 - y2) ** 2

print(max(distance, key=distance.get))