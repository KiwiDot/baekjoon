# 백준 24420번 ピアノコンクール (Piano Competition)
import sys
put = sys.stdin.readline

N = int(put())
A = [int(_) for _ in put().split()]

print(sum(A) - max(A) - min(A))