# 백준 18786번 Triangles (Bronze)
import sys
put = sys.stdin.readline

N = int(put())
XY = [[int(_) for _ in put().split()] for i in range(N)]
maximum = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            x3, y3 = XY[k]
            x = list({x1, x2, x3})
            y = list({y1, y2, y3})

            if len(x) == 2 and len(y) == 2:
                maximum = max(maximum, abs(x[0] - x[1]) * abs(y[0] - y[1]))

print(maximum)