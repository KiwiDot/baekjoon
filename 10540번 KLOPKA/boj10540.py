# 백준 10540번 KLOPKA
import sys
put = sys.stdin.readline

N = int(put())
x, y = [], []

while N:
    N -= 1
    X, Y = map(int, put().split())
    x.append(X)
    y.append(Y)

X = max(x) - min(x)
Y = max(y) - min(y)

print(max(X, Y) ** 2)