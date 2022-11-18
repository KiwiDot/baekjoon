# 백준 18416번 最長昇順連続部分列 (Longest Ascending Contiguous Subsequence)
import sys
put = sys.stdin.readline

N = int(put())
A = [int(_) for _ in put().split()]
a = []
cnt = 1

for i in range(1, len(A)):
    if A[i-1] > A[i]:
        a.append(cnt)
        cnt = 1
    else:
        cnt += 1

a.append(cnt)
print(max(a))