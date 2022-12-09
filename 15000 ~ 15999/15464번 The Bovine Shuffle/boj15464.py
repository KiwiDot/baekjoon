# 백준 15464번 The Bovine Shuffle
import sys
put = sys.stdin.readline

N = int(put())
a = [int(_) for _ in put().split()]
cow = put().split()

for i in range(3):
    cow = [cow[i-1] for i in a]

for i in cow:
    print(i)