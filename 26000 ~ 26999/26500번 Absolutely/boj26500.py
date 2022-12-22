# 백준 26500번 Absolutely
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    a, b = map(float, put().split())
    print("{:.1f}".format(abs(a - b)))