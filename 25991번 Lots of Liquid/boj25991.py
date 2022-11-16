# 백준 25991번 Lots of Liquid
import sys
put = sys.stdin.readline

n = int(put())
c = [float(_) ** 3 for _ in put().split()]

print(sum(c) ** (1/3))