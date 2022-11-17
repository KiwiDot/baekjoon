# 백준 11606번 Egg Drop
import sys
put = sys.stdin.readline

n, k = map(int, put().split())
x, y = 2, k-1

while n:
    n -= 1
    data = put().split()

    if data[1] == "SAFE":
        x = max(x, int(data[0])+1)

    else:
        y = min(y, int(data[0])-1)

print(x, y)