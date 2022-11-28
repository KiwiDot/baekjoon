# 백준 4482번 Tetrahedral Stacks of Cannonballs
import sys
put = sys.stdin.readline

n = int(put())

for i in range(1, n+1):
    cnt = 0
    t = int(put())

    for j in range(1, t+1):
        cnt += j * (j + 1) // 2

    print("{}: {} {}".format(i, t, cnt))

