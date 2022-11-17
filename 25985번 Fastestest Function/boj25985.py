# 백준 25985번 Fastestest Function
import sys
put = sys.stdin.readline

x, y = map(int, put().split())
foo_x = x * (100 - y)
foo_y = y * (100 - x)

print(foo_x / foo_y)