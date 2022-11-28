# 백준 26082번 WARBOY
import sys
put = sys.stdin.readline

A, B, C = map(int, put().split())
answer = B // A * C * 3

print(answer)