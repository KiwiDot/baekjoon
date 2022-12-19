# 백준 7326번 Number Steps
import sys
put = sys.stdin.readline

N = int(put())

while N:
    N -= 1
    x, y = map(int, put().split())

    if x >= 0 and y >= 0 and (x == y or x - y == 2):
        if x % 2:
            print(x + y - 1)
        else:
            print(x + y)

    else:
        print("No Number")