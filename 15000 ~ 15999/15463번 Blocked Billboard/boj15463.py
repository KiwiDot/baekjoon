# 백준 15463번 Blocked Billboard
import sys
put = sys.stdin.readline

x1, y1, x2, y2 = map(int, put().split())
x3, y3, x4, y4 = map(int, put().split())
x5, y5, x6, y6 = map(int, put().split())

set1 = set()
set2 = set()
set3 = set()

for x in range(x1, x2):
    for y in range(y1, y2):
        set1.add((x, y))

for x in range(x3, x4):
    for y in range(y3, y4):
        set2.add((x, y))

for x in range(x5, x6):
    for y in range(y5, y6):
        set3.add((x, y))

print(len(set1 - set3) + len(set2 - set3))