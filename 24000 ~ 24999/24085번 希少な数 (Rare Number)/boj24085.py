# 백준 24085번 希少な数 (Rare Number)
import sys
put = sys.stdin.readline

N = int(put())
A = [int(_) for _ in put().split()]
a = cnt = 101

for i in sorted(list(set(A))):
    cnt_a = A.count(i)
    if cnt > cnt_a:
        cnt = cnt_a
        a = i

print(a)