# 백준 5341번 Pyramids
import sys
put = sys.stdin.readline

pyramids = [0]
p = 0

while True:
    n = int(put())
    if not n:
        break

    if n > p:
        for i in range(n-p):
            p += 1
            pyramids.append(pyramids[-1] + p)

    print(pyramids[n])