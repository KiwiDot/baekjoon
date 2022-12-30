# 백준 14456번 Hoof, Paper, Scissors (Bronze)
import sys
put = sys.stdin.readline

N = int(put())
cnt1 = cnt2 = 0

while N:
    N -= 1
    c1, c2 = map(int, put().split())

    if c1 == c2:
        continue

    if c1 - c2 == 1 or c1 - c2 == -2:
        cnt1 += 1
    else:
        cnt2 += 1

print(max(cnt1, cnt2))