# 백준 6845번 Federal Voting Age
import sys
put = sys.stdin.readline

n = int(put())

while n:
    n -= 1
    y, m, d = map(int, put().split())

    if y < 1989:
        print("Yes")

    elif y == 1989:
        if m * 100 + d <= 227:
            print("Yes")
        else:
            print("No")
    else:
        print("No")