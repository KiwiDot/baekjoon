# 백준 26566번 Pizza
import sys
import math
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    A1, P1 = map(int, put().split())
    R1, P2 = map(int, put().split())
    a = P1 / A1
    r = P2 / (R1 * R1 * math.pi)

    if a < r:
        print("Slice of pizza")
    else:
        print("Whole pizza")