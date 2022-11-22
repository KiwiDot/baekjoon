# 백준 24927번 Is It Even?
import sys
put = sys.stdin.readline

N, K = map(int, put().split())
k = 0

while N:
    N -= 1
    x = int(put())

    while x % 2 == 0:
        x //= 2
        k += 1

print(1 if k >= K else 0)