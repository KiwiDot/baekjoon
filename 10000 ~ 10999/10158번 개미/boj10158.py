# 백준 10158번 개미
import sys
put = sys.stdin.readline

w, h = map(int, put().split())
p, q = map(int, put().split())
t = int(put())

p = w - abs((p + t) % (w * 2) - w)
q = h - abs((q + t) % (h * 2) - h)

print(p, q)
