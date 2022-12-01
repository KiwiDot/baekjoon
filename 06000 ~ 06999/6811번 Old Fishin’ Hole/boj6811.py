# 백준 6811번 Old Fishin’ Hole
import sys
put = sys.stdin.readline

p1 = int(put())
p2 = int(put())
p3 = int(put())
total = int(put())
cnt = 0

for i1 in range(total//p1 + 1):
    for i2 in range(total//p2 + 1):
        for i3 in range(total//p3 + 1):
            if 0 < p1 * i1 + p2 * i2 + p3 * i3 <= total:
                print("{} Brown Trout, {} Northern Pike, {} Yellow Pickerel".format(i1, i2, i3))
                cnt += 1

print("Number of ways to catch fish: {}".format(cnt))