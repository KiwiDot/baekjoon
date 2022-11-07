# 백준 23175번 Histogram Sequence 3
import sys
put = sys.stdin.readline

m = int(put())
a = []
b = [int(_) for _ in put().split()]
idx = 0

while idx < len(b):
    a.append(str(b[idx]))
    idx += b[idx]

print(' '.join(a))