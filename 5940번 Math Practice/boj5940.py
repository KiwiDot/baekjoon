# 백준 5940번 Math Practice
import sys
put = sys.stdin.readline

A, B = map(int, put().split())
E = 0

for i in range(A+1, 63):
    a = str(2 ** i)[0]
    if int(a) == B:
        E = i
        break

print(E)