# 백준 26592번 Triangle Height
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    a, b = map(float, put().split())
    h = a * 2 / b
    print("The height of the triangle is {:.2f} units".format(h))