# 백준 15803번 PLAYERJINAH’S BOTTLEGROUNDS
import sys
put = sys.stdin.readline

x1, y1 = map(int, put().split())
x2, y2 = map(int, put().split())
x3, y3 = map(int, put().split())

if (x1 - x2) * (y2 - y3) == (y1 - y2) * (x2 - x3):
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")
