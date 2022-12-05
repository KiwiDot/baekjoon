# 백준 11999번 Milk Pails (Bronze)
import sys
put = sys.stdin.readline

X, Y, M = map(int, put().split())
x = M // X + 1
y = M // Y + 1
m = 0

for i in range(x):
    for j in range(y):
        if X * i + Y * j > M:
            break

        m = max(m, X * i + Y * j)

print(m)