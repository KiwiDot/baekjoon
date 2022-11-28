# 백준 24074번 分割 (Split)
import sys
put = sys.stdin.readline

N = int(put())
A = [int(_) for _ in put().split()]

idx = A.index(max(A))
print(sum(A[:idx]))
print(sum(A[idx+1:]))