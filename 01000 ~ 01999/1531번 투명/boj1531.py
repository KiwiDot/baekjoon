# 백준 1531번 투명
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
n = {}
invisible = set()

while N:
    N -= 1
    x1, y1, x2, y2 = map(int, put().split())
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x, y) in n:
                n[(x, y)] += 1

            else:
                n[(x, y)] = 1

            if n[(x, y)] > M:
                invisible.add((x, y))

print(len(invisible))