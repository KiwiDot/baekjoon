# 백준 16728번 Chaarshanbegaan at Cafebazaar
import sys
put = sys.stdin.readline

N = int(put())
D = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]
score = 0

while N:
    N -= 1
    x, y = map(int, put().split())
    d = x ** 2 + y ** 2

    for i in range(10):
        if d <= D[i] ** 2:
            score += 10 - i
            break

print(score)