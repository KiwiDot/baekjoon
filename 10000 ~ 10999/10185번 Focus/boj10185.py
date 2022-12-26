# 백준 10185번 Focus
import sys
put = sys.stdin.readline

t = int(put())

while t:
    t -= 1
    p, q = map(int, put().split())
    f = p * q / (p + q)
    print("f = {:.1f}".format(f))