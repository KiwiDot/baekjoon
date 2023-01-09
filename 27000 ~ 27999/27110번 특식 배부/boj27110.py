# 백준 27110번 특식 배부
import sys
put = sys.stdin.readline

N = int(put())
A, B, C = map(int, put().split())

print(min(A, N) + min(B, N) + min(C, N))