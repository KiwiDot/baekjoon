# 백준 19604번 Art
import sys
put = sys.stdin.readline

N = int(put())
x1 = y1 = 100
x2 = y2 = 0

while N:
    N -= 1
    X, Y = map(int, put().split(','))

    x1 = min(x1, X)
    y1 = min(y1, Y)
    x2 = max(x2, X)
    y2 = max(y2, Y)

print("{},{}".format(x1-1, y1-1))
print("{},{}".format(x2+1, y2+1))