# 백준 6887번 Squares
import sys
put = sys.stdin.readline

tile = int(put())
side = int(tile ** 0.5)

print("The largest square has side length {}.".format(side))