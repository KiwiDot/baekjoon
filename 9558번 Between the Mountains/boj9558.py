# 백준 9558번 Between the Mountains
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    n1 = [int(_) for _ in put().split()][1:]
    n2 = [int(_) for _ in put().split()][1:]
    diff = 1000000

    for i in n1:
        for j in n2:
            diff = min(diff, abs(i - j))

    print(diff)