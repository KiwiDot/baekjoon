# 백준 26532번 Acres
import sys
put = sys.stdin.readline

x, y = map(int, put().split())
acre = x * y // 4840 + 1 if x * y % 4840 else x * y // 4840

print(acre // 5 + 1 if acre % 5 else acre // 5)