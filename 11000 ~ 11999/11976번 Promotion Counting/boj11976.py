# 백준 11976번 Promotion Counting
import sys
put = sys.stdin.readline

b1, b2 = map(int, put().split())
s1, s2 = map(int, put().split())
g1, g2 = map(int, put().split())
p1, p2 = map(int, put().split())

p = p2 - p1
g = g2 - g1 + p
s = s2 - s1 + g

print(s)
print(g)
print(p)