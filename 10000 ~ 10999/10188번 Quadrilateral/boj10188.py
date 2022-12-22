# 백준 10188번 Quadrilateral
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    l, w = map(int, put().split())

    for i in range(w):
        print('X' * l)

    print()