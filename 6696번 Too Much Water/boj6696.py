# 백준 6696번 Too Much Water
import sys
import math
put = sys.stdin.readline

while True:
    X, Y = map(float, put().split())
    if X == Y == 0:
        break

    Z = (X ** 2 + Y ** 2) * math.pi
    Z = int(Z / 100) + 1 if Z % 100 else Z // 100

    print("The property will be flooded in hour {}.".format(Z))