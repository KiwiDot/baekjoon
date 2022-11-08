# 백준 4890번 Tiles of Tetris, NOT!
import sys
import math
put = sys.stdin.readline

while True:
    W, H = map(int, put().split())
    if W == H == 0:
        break

    lcm = math.lcm(W, H)
    w = lcm // W
    h = lcm // H

    print(w * h)