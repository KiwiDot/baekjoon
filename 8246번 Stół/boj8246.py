# 백준 8246번 Stół
import sys
put = sys.stdin.readline

A, B, K = map(int, put().split())
a, b = A // K, B // K
a_ = A // K - 2 if A // K > 2 else 0
b_ = B // K - 2 if B // K > 2 else 0

print(a * b - a_ * b_)