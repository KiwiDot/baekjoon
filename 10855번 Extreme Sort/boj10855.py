# 백준 10855번 Extreme Sort
import sys
put = sys.stdin.readline

N = int(put())
a = [int(_) for _ in put().split()]

if a == sorted(a):
    print("yes")
else:
    print("no")