# 백준 26741번 Farma
import sys
put = sys.stdin.readline

X, Y = map(int, put().split())
chicken = (4 * X - Y) // 2
cow = X - chicken

print(chicken, cow)