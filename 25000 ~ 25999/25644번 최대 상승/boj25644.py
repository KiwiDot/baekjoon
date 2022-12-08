# 백준 25644번 최대 상승
import sys
put = sys.stdin.readline

N = int(put())
a = [int(_) for _ in put().split()]
minimum = 10 ** 9
maximum = 0

for i in range(N):
    minimum = min(minimum, a[i])
    maximum = max(maximum, a[i] - minimum)

print(maximum)