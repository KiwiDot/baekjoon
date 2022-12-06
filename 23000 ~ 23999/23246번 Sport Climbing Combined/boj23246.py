# 백준 23246번 Sport Climbing Combined
import sys
put = sys.stdin.readline

n = int(put())
athlete = []

while n:
    n -= 1
    b, p, q, r = map(int, put().split())
    athlete += [[p * q * r, p + q + r, b]]

athlete.sort()
for i in range(3):
    print(athlete[i][2], end=' ')
print()